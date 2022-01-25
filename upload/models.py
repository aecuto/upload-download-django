from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Upload(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    password = models.CharField(max_length=255, blank=True, null=True)
    max_downloads = models.IntegerField()
    expire_date = models.DateTimeField()
    file_name = models.CharField(max_length=255, blank=True, null=True)
    upload_path = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("download", args=(self.id,))

class Download(models.Model):
    date = models.DateTimeField()
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)

