from datetime import datetime
from django.core.management.base import BaseCommand
import pytz

from upload.models import Upload

class Command(BaseCommand):
    help = 'Remove expired files'

    def handle(self, *args, **options):
        list = Upload.objects.all()
        for upload in list:
            if datetime.now(pytz.UTC) > upload.expire_date:
                print("remove : " + str(upload.id))

        # Upload._base_manager.filter(expire_date__gte=Now()).delete()