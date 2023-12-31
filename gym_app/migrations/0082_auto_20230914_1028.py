# Generated by Django 3.2.9 on 2023-09-14 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0081_alter_extendedusermodel_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='grand_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='extendedusermodel',
            name='amount_paid',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='paid amount'),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 9, 14)),
        ),
    ]
