# Generated by Django 2.1.5 on 2019-04-28 16:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleitem',
            name='additional_speakers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='additional speakers'),
        ),
    ]