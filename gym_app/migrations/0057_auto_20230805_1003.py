# Generated by Django 3.2.9 on 2023-08-05 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0056_alter_salary_management_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary_management',
            name='balance',
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 8, 5)),
        ),
    ]
