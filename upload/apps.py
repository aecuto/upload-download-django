from django.apps import AppConfig
from .scheduler.run_script import run_continuously

class UploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload'
    def ready(self):
        run_continuously()



