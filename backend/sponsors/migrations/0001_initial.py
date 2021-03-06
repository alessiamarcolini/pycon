# Generated by Django 2.2.4 on 2019-08-30 21:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conferences', '0007_auto_20190811_1953'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor_levels', to='conferences.Conference', verbose_name='conference')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'unique_together': {('name', 'conference')},
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('link', models.URLField(blank=True, verbose_name='published')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sponsors', verbose_name='image')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsors', to='sponsors.SponsorLevel', verbose_name='level')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
