# Generated by Django 2.2.8 on 2019-12-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='send_date',
            field=models.DateTimeField(null=True, verbose_name='send date'),
        ),
    ]
