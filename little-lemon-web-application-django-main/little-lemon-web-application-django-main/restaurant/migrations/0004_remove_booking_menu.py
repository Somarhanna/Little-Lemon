# Generated by Django 5.0 on 2023-12-12 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_booking_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='menu',
        ),
    ]