
from django.core.management.base import BaseCommand
from django.utils import timezone

from upload.models import Upload
from upload.utils import handle_delete_file

class Command(BaseCommand):
    help = 'Remove expired files'

    def handle(self, *args, **options):
        list = Upload.objects.filter(expire_date__lte=timezone.now())
        for upload in list:
            print(f"auto delete: removed file {upload.file_name} (id={upload.id})") 
            handle_delete_file(upload.upload_path)
            upload.delete()
