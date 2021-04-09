from django.urls import path, include

from . import views

urlpatterns = [
    # Clinics
    path('clinic/register/', views.RegisterClinic.as_view(),
         name='Register Clinics'),
    path('clinic/login/', views.LoginClinic.as_view(), name='Login Clinics'),
    path('clinic/<int:id>/', views.GetClinic.as_view(), name='Get Clinic'),
    path('clinic/', views.GetAllClinics.as_view(), name='Get Clinics'),
    # Pets
    path('pet/register/', views.RegisterPet.as_view(), name='Register Pet'),
    path('pet/<int:user_id>/<int:pet_id>/',
         views.GetPet.as_view(), name='Get Pet from a user'),
    path('pets/<int:id>/', views.GetPets.as_view(),
         name='Get All Pets from a user'),
    # Users
    path('user/register/', views.RegisterUser.as_view(), name='Register User'),
    path('user/login/', views.LoginUser.as_view(), name='Login Users'),
    path('user/<user_id>/', views.GetUser.as_view(), name='Get User'),
    # Booking
    path('booking/book/', views.Booking.as_view(), name='Register Booking'),
    path('booking/time/', views.BookingTime.as_view(), name='Check Booking Time'),

    # Appointments
    path('user/appointment/<int:user_id>', views.UserAppointment.as_view(), name='User Appointments'),
    path('clinic/appointment/<int:clinic_id>', views.ClinicAppointment.as_view(), name='Clinic Appointments'),
    
]
