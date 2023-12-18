# Generated by Django 4.2.1 on 2023-06-20 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0017_schedulestatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizedplan',
            name='status',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.schedulestatus'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='status',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.schedulestatus'),
        ),
    ]