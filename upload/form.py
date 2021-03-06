from django import forms
from .models import Upload
from .form_validator import filesize_validate

class UploadForm(forms.ModelForm):
    file = forms.FileField(validators=[filesize_validate])
    max_downloads = forms.ChoiceField(
        choices=[
            (1, "1 download"),
            (2, "2 downloads"),
            (3, "3 downloads"),
            (4, "4 downloads"),
            (5, "5 downloads"),
            (20, "20 downloads"),
            (50, "50 downloads"),
            (100, "100 downloads"),
        ]
    )
    expire_duration = forms.ChoiceField(
        choices=[
            (5 * 60, "5 minutes"),
            (60 * 60, "1 hour"),
            (24 * 60 * 60, "1 day"),
            (7 * 24 * 60 * 60, "7 days"),
        ]
    )

    class Meta:
        model = Upload
        fields = ["file", "max_downloads", "expire_duration","password"]
        widgets = {
            "password": forms.PasswordInput(),
        }
        help_texts = {
            "password": "(optional)",
        }
