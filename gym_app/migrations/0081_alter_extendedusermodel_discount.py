# Generated by Django 3.2.9 on 2023-09-13 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0080_auto_20230913_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='discount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
