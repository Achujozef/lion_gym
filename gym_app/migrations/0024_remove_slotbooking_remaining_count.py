# Generated by Django 4.2.1 on 2023-07-07 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0023_alter_slotbooking_remaining_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotbooking',
            name='remaining_count',
        ),
    ]
