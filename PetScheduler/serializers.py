from rest_framework import serializers
from . import models as mdls


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdls.User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'password',
                  'mobile_number', 'address', 'city', 'postal_code', 'apartement_suite_code']


class UserSerializerPartial(serializers.ModelSerializer):
    class Meta:
        model = mdls.User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'mobile_number',
                  'address', 'city', 'postal_code', 'apartement_suite_code']


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdls.Pet
        fields = ['pet_id', 'pet_name', 'age',
                  'gender', 'breed', 'species', 'owner_id']


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdls.Clinic
        fields = '__all__'


class ClinicSerializerNoPassword(serializers.ModelSerializer):
    class Meta:
        model = mdls.Clinic
        fields = ['clinic_id', 'clinic_name', 'address', 'mobile_number', 'email', 'city',
                  'postal_code', 'clinic_website', 'specialities', 'available_days', 'available_hours']


class SimpleClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdls.Clinic
        fields = ['clinic_id', 'clinic_name', 'address', 'mobile_number', 'email',
                  'city', 'postal_code', 'clinic_website', 'available_days', 'available_hours']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = mdls.Booking
        fields = '__all__'
