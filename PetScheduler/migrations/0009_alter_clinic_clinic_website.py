# Generated by Django 3.2 on 2021-04-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetScheduler', '0008_auto_20210314_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='clinic_website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
