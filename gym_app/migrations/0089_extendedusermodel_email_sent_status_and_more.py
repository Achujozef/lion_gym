# Generated by Django 4.2.1 on 2023-09-29 05:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0088_alter_prefferedtime_reset_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='email_sent_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 9, 29)),
        ),
    ]
