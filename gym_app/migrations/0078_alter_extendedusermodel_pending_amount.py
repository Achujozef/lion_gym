# Generated by Django 4.2.1 on 2023-09-12 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0077_alter_prefferedtime_reset_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='pending_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]