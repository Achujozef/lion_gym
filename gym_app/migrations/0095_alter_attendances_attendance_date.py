# Generated by Django 4.2.1 on 2023-10-06 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0094_attendances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendances',
            name='attendance_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
