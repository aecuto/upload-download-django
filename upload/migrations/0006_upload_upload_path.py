# Generated by Django 4.0.1 on 2022-01-22 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_rename_upload_path_upload_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='upload_path',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
