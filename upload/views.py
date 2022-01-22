
from datetime import datetime, timedelta
import os
from django.views.generic import CreateView, DetailView

from django.http import FileResponse, HttpResponse

from upload.utils import handle_uploaded_file

from .form import UploadForm
from .models import Upload


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

        upload_path = handle_uploaded_file(file)

        form.instance.expire_date = datetime.now() + timedelta(seconds=int(duration))
        form.instance.upload_path = upload_path

        return super().form_valid(form)


class Download(DetailView):
    model = Upload

    # TODO:
    # Make it so that you can't download expired files

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        print(self.object.upload_path)

        if self.object.password is not None:
            if self.request.POST.get("password") != "password":
                return HttpResponse("invalid password")


        response = FileResponse(open(self.object.upload_path, 'rb'))
        return response
        return HttpResponse("todo")

        # TODO:
        # 1) Delete file when max_downloads is done
        # 2) Verify password securely
        # 3) Actually send the download


class Delete(DetailView):
    model = Upload
    template_name = "upload/delete.html"

    def post(self, *args, **kwargs):
        self.object = self.get_object()
        # TODO: Actually delete fil
        self.object.delete()
        return HttpResponse("Deleted!")
