# Generated by Django 4.2.1 on 2023-10-26 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0101_remove_enquiry_membership_expiry_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='membership_expiry_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Closed', 'Closed')], default='Pending', max_length=25),
        ),
    ]
