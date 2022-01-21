
from django.views.generic import CreateView, DetailView

from django.http import HttpResponse

from .form import UploadForm
from .models import Upload


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

    

class UploadPage(CreateView):
    model = Upload
    form_class = UploadForm

    # TODO:
    # 1) Convert expire_duration to expire_date
    # 2) Upload and save
    # 3) Generate download and delete link


class Download(DetailView):
    model = Upload

    # TODO:
    # Make it so that you can't download expired files

    def post(self, *args, **kwargs):
        self.object = self.get_object()

        if self.object.password is not None:
            if self.request.POST.get("password") != "password":
                return HttpResponse("invalid password")

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