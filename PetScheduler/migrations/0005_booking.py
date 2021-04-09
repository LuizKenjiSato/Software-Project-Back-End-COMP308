# Generated by Django 3.0.8 on 2021-03-13 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PetScheduler', '0004_auto_20210307_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=300)),
                ('date', models.CharField(max_length=3)),
                ('month', models.CharField(max_length=10)),
                ('time_selected', models.CharField(max_length=10)),
                ('clinic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetScheduler.Clinic')),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetScheduler.User')),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetScheduler.Pet')),
            ],
        ),
    ]