# Generated by Django 4.2.9 on 2024-01-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0016_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='resolved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
