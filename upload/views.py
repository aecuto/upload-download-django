
from django.utils import timezone
from django.views.generic import CreateView, DetailView
from django.contrib.auth.hashers import make_password, check_password
from django.http import FileResponse, HttpResponse
from django.urls import reverse
from django.utils import timezone

import pytz
from datetime import datetime, timedelta

from .form import UploadForm
from .models import Upload, Download as DownloadModel
from upload.utils import handle_delete_file, handle_uploaded_file, validate_file_size



class UploadPage(CreateView):
    model = Upload
    form_class = UploadForm

    def form_valid(self, form):
        file = self.request.FILES['file']
        duration = self.request.POST.get('expire_duration')
        password = self.request.POST.get('password')

        if validate_file_size(file):
            return HttpResponse("The maximum file size that can be uploaded is 100MB")

        upload_path = handle_uploaded_file(file)

        form.instance.expire_date = timezone.now() + timedelta(seconds=int(duration))
        form.instance.file_name = file.name
        form.instance.upload_path = upload_path
        form.instance.user = self.request.user
        form.instance.password = make_password(password)

        return super().form_valid(form)


class Download(DetailView):
    model = Upload

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if timezone.now() > self.object.expire_date:
            handle_delete_file(self.object.upload_path)
            self.object.delete()
            return HttpResponse("File Expiry Dates and auto delete.")

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


    def get_context_data(self, *args, **kwargs):
        self.object = self.get_object()

        context = super().get_context_data(*args, **kwargs)
        download_url = self.request.build_absolute_uri(reverse("download", args=(self.object.id,)))
        delete_url = self.request.build_absolute_uri(reverse("delete", args=(self.object.id,)))
        context["download_url"] = download_url
        context["delete_url"] = delete_url
        return context

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        if self.object.password is not None:
            password = self.request.POST.get("password")
            if not check_password(password,self.object.password):
                return HttpResponse("invalid password")

        count_download = DownloadModel.objects.filter(upload_id=self.object.id).count()

        if count_download >= self.object.max_downloads:
            handle_delete_file(self.object.upload_path)
            self.object.delete()
            return HttpResponse("reached the file's maximum number of downloads")

        download = DownloadModel(date=timezone.now(), upload=self.object)
        download.save()

        return FileResponse(open(self.object.upload_path, 'rb'),filename=self.object.file_name)

class Delete(DetailView):
    model = Upload
    template_name = "upload/delete.html"

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        handle_delete_file(self.object.upload_path)
        self.object.delete()
        return HttpResponse("Deleted!")
