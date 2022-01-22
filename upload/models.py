from django.db import models
from django.urls import reverse


class Upload(models.Model):
    password = models.CharField(max_length=255, blank=True, null=True)
    max_downloads = models.IntegerField()
    expire_date = models.DateTimeField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    upload_path = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("download", args=(self.id,))

class Download(models.Model):
    date = models.DateTimeField()
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)

