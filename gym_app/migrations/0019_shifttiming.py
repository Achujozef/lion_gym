# Generated by Django 4.2.1 on 2023-07-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0018_customizedplan_status_schedule_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftTiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]