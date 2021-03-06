# Generated by Django 2.2.8 on 2020-03-04 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0023_scheduleitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleitem',
            name='status',
            field=models.CharField(choices=[('confirmed', 'Confirmed'), ('maybe', 'Maybe'), ('waiting_confirmation', 'Waiting confirmation'), ('cancelled', 'Cancelled')], default='waiting_confirmation', max_length=25, verbose_name='status'),
        ),
    ]
