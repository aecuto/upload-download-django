# Generated by Django 4.0.1 on 2022-01-25 11:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_upload_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
