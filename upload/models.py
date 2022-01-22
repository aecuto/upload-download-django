from django.db import models
from django.urls import reverse


class Upload(models.Model):
		password = models.CharField(max_length=255, blank=True, null=True)
		max_downloads = models.IntegerField()
		expire_date = models.DateTimeField()
		upload_path = models.CharField(max_length=255, blank=True, null=True)

		def get_absolute_url(self):
				return reverse("download", args=(self.id,))

