# Generated by Django 3.2.9 on 2023-08-22 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0067_auto_20230822_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='fitness_goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.goal'),
        ),
    ]
