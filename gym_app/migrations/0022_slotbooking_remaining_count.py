# Generated by Django 4.2.1 on 2023-07-07 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0021_prefferedtime_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='slotbooking',
            name='remaining_count',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='remaining_count', to='gym_app.prefferedtime'),
            preserve_default=False,
        ),
    ]
