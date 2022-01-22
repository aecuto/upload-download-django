
from datetime import datetime, timedelta

from telnetlib import DO
from django.forms import ValidationError
from django.views.generic import CreateView, DetailView

from django.http import FileResponse, HttpResponse
import pytz

from upload.utils import get_upload_path, handle_delete_file, handle_uploaded_file, validate_file_size

from .form import UploadForm
from .models import Upload, Download as DownloadModel

utc=pytz.UTC

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UploadPage(CreateView):
    model = Upload
    form_class = UploadForm
    # TODO:
    # 1) Convert expire_duration to expire_date x
    # 2) Upload and save 
    # 3) Generate download and delete link 

    def form_valid(self, form):
        duration = self.request.POST.get('expire_duration')
        file = self.request.FILES['file']

        if validate_file_size(file):
            return HttpResponse("The maximum file size that can be uploaded is 100MB")

        upload_file_name = handle_uploaded_file(file)

        form.instance.expire_date = datetime.now() + timedelta(seconds=int(duration))
        form.instance.file_name = file.name
        form.instance.upload_path = get_upload_path(upload_file_name)

        return super().form_valid(form)


class Download(DetailView):
    model = Upload

    # TODO:
    # Make it so that you can't download expired files

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        if self.object.password is not None:
            if self.request.POST.get("password") != "password":
                handle_delete_file(self.object.upload_path)
                return HttpResponse("invalid password")

        if datetime.now(utc) > self.object.expire_date:
            handle_delete_file(self.object.upload_path)
            return HttpResponse("file expiry")

        count_download = DownloadModel.objects.filter(upload_id=self.object.id).count()

        if count_download >= self.object.max_downloads:
            handle_delete_file(self.object.upload_path)
            return HttpResponse("reached the file's maximum number of downloads")

        download = DownloadModel(date=datetime.now(), upload=self.object)
        download.save()

        return FileResponse(open(self.object.upload_path, 'rb'),filename=self.object.file_name)

        # TODO:
        # 1) Delete file when max_downloads is done
        # 2) Verify password securely
        # 3) Actually send the download


class Delete(DetailView):
    model = Upload
    template_name = "upload/delete.html"

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        handle_delete_file(self.object.upload_path)
        self.object.delete()
        return HttpResponse("Deleted!")
