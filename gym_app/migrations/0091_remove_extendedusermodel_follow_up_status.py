# Generated by Django 4.2.1 on 2023-10-04 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0090_extendedusermodel_follow_up_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendedusermodel',
            name='follow_up_status',
        ),
    ]
