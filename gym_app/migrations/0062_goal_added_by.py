# Generated by Django 3.2.9 on 2023-08-11 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0061_alter_membershipplan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.bussinessownermodel'),
        ),
    ]
