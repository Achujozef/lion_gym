# Generated by Django 4.2.1 on 2023-08-03 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0049_id_proof_alter_prefferedtime_reset_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='id_proof_imagee',
            field=models.ImageField(blank=True, null=True, upload_to='ID Proofs'),
        ),
        migrations.AddField(
            model_name='extendedusermodel',
            name='id_prooff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.id_proof'),
        ),
    ]