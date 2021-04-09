from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=64)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=250)
    apartement_suite_code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return self.first_name


class Pet(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    breed = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name

# TODO add passsword


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    clinic_name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    mobile_number = models.CharField(max_length=64)
    email = models.EmailField(max_length=250)
    city = models.CharField(max_length=100, default='Toronto')
    postal_code = models.CharField(max_length=7, default='H0H0H0')
    password = models.CharField(max_length=250, default='password')
    clinic_website = models.URLField(max_length=255, blank=True, null=True)
    specialities = ArrayField(models.CharField(
        max_length=100), blank=True, null=True)
    available_days = ArrayField(models.CharField(max_length=100))
    available_hours = ArrayField(models.CharField(max_length=100))

    def __str__(self):
        return self.clinic_name


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    date = models.CharField(max_length=3)
    month = models.CharField(max_length=10)
    time_selected = models.CharField(max_length=10)
