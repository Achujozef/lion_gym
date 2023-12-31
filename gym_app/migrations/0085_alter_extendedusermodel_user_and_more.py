# Generated by Django 4.2.1 on 2023-09-19 12:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym_app', '0084_remove_extendedusermodel_add_on_plan_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extendeduser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 9, 19)),
        ),
    ]
