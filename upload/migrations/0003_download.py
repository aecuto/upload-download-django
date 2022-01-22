# Generated by Django 4.0.1 on 2022-01-22 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_upload_upload_path'),
    ]

    operations = [
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('upload_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.upload')),
            ],
        ),
    ]
