# Generated by Django 4.2.1 on 2023-09-19 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0086_alter_extendedusermodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendedusermodel',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extendedbusiness', to='gym_app.bussinessownermodel'),
        ),
    ]
