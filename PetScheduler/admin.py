from django.contrib import admin
from . import models 

admin.site.register([models.User, models.Clinic, models.Pet, models.Booking])
# Register your models here.
