# Generated by Django 3.2.9 on 2023-07-22 05:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0035_auto_20230719_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='membershipplan',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.bussinessownermodel'),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 7, 22)),
        ),
    ]