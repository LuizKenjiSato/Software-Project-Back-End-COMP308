# Generated by Django 3.0.8 on 2021-03-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetScheduler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apartement_suite_code',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
