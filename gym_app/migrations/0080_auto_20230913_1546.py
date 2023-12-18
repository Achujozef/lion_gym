# Generated by Django 3.2.9 on 2023-09-13 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0079_auto_20230913_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='admission_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='balance_due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='payment_mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.payment_mode'),
        ),
    ]
