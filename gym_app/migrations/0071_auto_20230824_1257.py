# Generated by Django 3.2.9 on 2023-08-24 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0070_auto_20230823_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_management',
            name='advance_paid',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='salary_management',
            name='personal_training_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 8, 24)),
        ),
    ]
