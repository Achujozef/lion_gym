# Generated by Django 4.2.1 on 2023-06-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0009_extendedusermodel_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='assigntrainer',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.bussinessownermodel'),
        ),
    ]
