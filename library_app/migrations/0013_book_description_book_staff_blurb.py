# Generated by Django 4.2.9 on 2024-01-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0012_event_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='staff_blurb',
            field=models.TextField(blank=True),
        ),
    ]
