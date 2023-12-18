# Generated by Django 3.2.9 on 2023-05-29 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0005_bussinessownermodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('features', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AssignTrainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(blank=True, null=True)),
                ('exp_date', models.DateField(blank=True, null=True)),
                ('Iinitaial_amount', models.IntegerField(blank=True, null=True)),
                ('pending_amount', models.IntegerField(blank=True, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member', to='gym_app.extendedusermodel')),
                ('membership_plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_app.membershipplan')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigntrainer', to='gym_app.extendedusermodel')),
            ],
        ),
    ]