# Generated by Django 2.2.12 on 2020-04-29 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='TaskerLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('tasker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taskerlocation_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
    ]
