# Generated by Django 4.2.1 on 2023-06-09 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0014_activitylevel_goal_memberprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('schedule_date', models.DateField(blank=True, null=True)),
                ('time_slot_field', models.TimeField()),
                ('workout_type', models.CharField(blank=True, max_length=100, null=True)),
                ('members', models.ManyToManyField(related_name='schedules', to='gym_app.assigntrainer')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.extendedusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CustomizedPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calorie_intake', models.FloatField(null=True)),
                ('goal', models.CharField(blank=True, max_length=20, null=True)),
                ('meal_options', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dietmember', to='gym_app.assigntrainer')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diettrainer', to='gym_app.extendedusermodel')),
            ],
        ),
        migrations.CreateModel(
            name='CommonDietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.TextField()),
                ('snack_mrng', models.TextField()),
                ('lunch', models.TextField()),
                ('snack', models.TextField()),
                ('dinner', models.TextField()),
                ('optional_beverages', models.TextField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.week')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goalcommon', to='gym_app.goal')),
            ],
        ),
    ]
