# Generated by Django 4.2.1 on 2023-06-02 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0010_assigntrainer_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assigntrainer',
            name='added_by',
        ),
    ]
