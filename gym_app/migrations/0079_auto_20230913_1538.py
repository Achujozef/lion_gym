# Generated by Django 3.2.9 on 2023-09-13 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0078_alter_extendedusermodel_pending_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment_mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='expected_join_date',
            field=models.DateField(blank=True, null=True, verbose_name='followup date'),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 9, 13)),
        ),
    ]
