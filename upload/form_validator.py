from django.core.exceptions import ValidationError

def filesize_validate(value):
    # 100MB - 104857600
    if value.size > 104857600:
        raise ValidationError('The maximum file size that can be uploaded is 100MB')