# Generated by Django 3.2.9 on 2023-08-05 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0057_auto_20230805_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_management',
            name='balance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
