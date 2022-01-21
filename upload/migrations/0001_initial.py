# Generated by Django 4.0.1 on 2022-01-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('max_downloads', models.IntegerField()),
                ('expire_date', models.DateTimeField()),
            ],
        ),
    ]
