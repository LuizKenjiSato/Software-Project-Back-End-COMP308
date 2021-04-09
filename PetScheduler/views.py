from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

import json

from . import models
from . import serializers

# Clinic


class RegisterClinic(APIView):
    def post(self, request, format=None):
        print(request.body)
        try:
            data = json.loads(request.body)
        except Exception as err:
            tmp = request.body.decode("utf-8")
            data = json.loads(tmp)
        if models.Clinic.objects.filter(email=data['email']).exists():
            return Response('An clinic wiht this email already exist', status.HTTP_403_FORBIDDEN)
        else:
            if 'specialities' not in data or data['specialities'] == "":
                clinic_serializer = serializers.SimpleClinicSerializer(
                    data=data)
            else:
                clinic_serializer = serializers.ClinicSerializer(data=data)

            if clinic_serializer.is_valid():
                clinic_serializer.save()
                return Response('Clinic created', status=status.HTTP_201_CREATED)
            else:
                print(clinic_serializer.errors)
                return Response('Something went wrong', status=status.HTTP_403_FORBIDDEN)


class LoginClinic(APIView):
    def post(self, request, format=None):
        print(request.body)
        try:
            data = json.loads(request.body)
        except Exception as err:
            tmp = request.body.decode("utf-8")
            data = json.loads(tmp)
        try:
            clinic_login = models.Clinic.objects.get(email=data['email'])
            if data['password'] == clinic_login.password:
                clinic_serializer = serializers.ClinicSerializerNoPassword(
                    clinic_login)
                return Response(clinic_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_403_FORBIDDEN)


class GetClinic(APIView):
    def get(self, request, id, format=None):
        clinic = models.Clinic.objects.get(clinic_id=id)
        clinic_serializer = serializers.ClinicSerializerNoPassword(clinic)

        return Response(clinic_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, id, format=None):
        data = request.data
        clinic = models.Clinic.objects.get(clinic_id=id)
        clinic_serializer = serializers.ClinicSerializerNoPassword(clinic, data=data, partial=True)

        if clinic_serializer.is_valid():
            clinic_serializer.save()
        else:
            print(clinic_serializer.errors)
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAllClinics(APIView):
    def get(self, request, format=None):
        all_clinics = models.Clinic.objects.all()
        clinics_serializer = serializers.ClinicSerializerNoPassword(
            all_clinics, many=True)

        return Response(clinics_serializer.data,  status=status.HTTP_200_OK)

# Pet


class RegisterPet(APIView):
    def post(self, request, format=None):
        print(request.body)
        try:
            data = json.loads(request.body)
        except Exception as err:
            tmp = request.body.decode("utf-8")
            data = json.loads(tmp)

        try:
            owner_id = models.User.objects.get(
                email=data['user_email']).user_id
            data['owner_id'] = owner_id
        except Exception as err:
            return Response('Something went wrong', status=status.HTTP_403_FORBIDDEN)

        if models.Pet.objects.filter(owner_id=owner_id).filter(pet_name=data['pet_name']).exists():
            return Response('Pet already register', status=status.HTTP_403_FORBIDDEN)
        else:
            pet_serializer = serializers.PetSerializer(data=data)
            if pet_serializer.is_valid():
                pet_serializer.save()
                return Response('Pet register', status=status.HTTP_201_CREATED)
            else:
                print(pet_serializer.errors)
                return Response('Something went wrong', status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_201_CREATED)


class GetPet(APIView):
    def get(self, request, user_id, pet_id, format=None):
        pet = models.Pet.objects.filter(
            owner_id=user_id).filter(pet_id=pet_id).get()
        pet_serializer = serializers.PetSerializer(pet)
        return Response(pet_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id, pet_id, format=None):
        data = request.data
        pet = models.Pet.objects.filter(
            owner_id=user_id).filter(pet_id=pet_id).get()
        pet_serializer = serializers.PetSerializer(pet, data=data, partial=True)

        if pet_serializer.is_valid():
            pet_serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, user_id, pet_id, format=None):
        pet = models.Pet.objects.filter(owner_id = user_id, pet_id = pet_id)
        if pet.exists():
            pet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('cannot delete pet, something went wrong', status=status.HTTP_400_BAD_REQUEST)
            
        

class GetPets(APIView):
    def get(self, request, id, format=None):
        pets = models.Pet.objects.filter(owner_id=id)
        pets_serializer = serializers.PetSerializer(pets, many=True)
        return Response(pets_serializer.data, status=status.HTTP_200_OK)

# User


class RegisterUser(APIView):
    def post(self, request, format=None):
        print(request.body)
        try:
            data = json.loads(request.body)
        except Exception as err:
            tmp = request.body.decode("utf-8")
            data = json.loads(tmp)

        if models.User.objects.filter(email=data['email']).exists():
            return Response('Account wiht this email already exist', status.HTTP_403_FORBIDDEN)
        else:
            user_serializer = serializers.UserSerializer(data=data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response('Account created', status=status.HTTP_201_CREATED)
            else:
                print(user_serializer.errors)
                return Response('Something went wrong', status=status.HTTP_403_FORBIDDEN)


class LoginUser(APIView):
    def post(self, request, format=None):
        print(request.body)
        try:
            data = json.loads(request.body)
        except Exception as err:
            tmp = request.body.decode("utf-8")
            data = json.loads(tmp)
        try:
            user_login = models.User.objects.get(email=data['email'])
            if data['password'] == user_login.password:
                user_serializer = serializers.UserSerializerPartial(user_login)
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_403_FORBIDDEN)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_403_FORBIDDEN)


class GetUser(APIView):
    def get(self, request, user_id, format=None):
        user = models.User.objects.get(user_id=user_id)
        user_serializer = serializers.UserSerializerPartial(user)
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    def put(self, request, user_id, format=None):
        data = request.data
        user = models.User.objects.get(user_id=user_id)
        user_serializer = serializers.UserSerializerPartial(user, data=data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Booking


class Booking(APIView):
    def post(self, request, format=None):
        data = request.data
        # print(data)
        if models.Booking.objects.filter(clinic_id=data['clinic_id']).filter(date=data['date']) \
                .filter(month=data['month']).filter(time_selected=data['time_selected']).exists():
            return Response('This time is already booked', status=status.HTTP_400_BAD_REQUEST)
        else:
            booking_serializer = serializers.BookingSerializer(data=data)
            if booking_serializer.is_valid():
                booking_serializer.save()
                return Response('Appointment Booked', status=status.HTTP_201_CREATED)


class BookingTime(APIView):
    def post(self, request, format=None):
        data = request.data

        booked_time = models.Booking.objects.filter(clinic_id=data['clinic_id']).filter(date=data['date']) \
            .filter(month=data['month'])

        booked_serializer = serializers.BookingSerializer(
            booked_time, many=True)
        booked_time = []
        for x in booked_serializer.data:
            booked_time.append(x['time_selected'])

        clinic = models.Clinic.objects.get(clinic_id=data['clinic_id'])
        clinic_serializer = serializers.ClinicSerializer(clinic).data

        for x in booked_time:
            try:
                clinic_serializer['available_hours'].remove(x)
            except Exception as err:
                print(err)
        return Response(clinic_serializer['available_hours'], status=status.HTTP_200_OK)

# TODO LOGIN for user/clinic => add hash table

# Appointments
class UserAppointment(APIView):
    def get(self, request, user_id, format=None):
        appointments = models.Booking.objects.filter(owner_id = user_id)
        if appointments.exists():
            appointments_serializer = serializers.BookingSerializer(appointments, many=True)
            for x in appointments_serializer.data:
                ## Pet Info
                pet_info = models.Pet.objects.get(pet_id = x['pet_id'])
                del x['pet_id']
                x['pet_info'] = serializers.PetSerializer(pet_info).data
                ## Clinic Info
                clinic_info = models.Clinic.objects.get(clinic_id = x['clinic_id'])
                del x['clinic_id']
                x['clinic_info'] = serializers.ClinicSerializerNoPassword(clinic_info).data
            return Response(appointments_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class ClinicAppointment(APIView):
    def get(self, request, clinic_id, format=None):
        appointments = models.Booking.objects.filter(clinic_id = clinic_id)
        if appointments.exists():
            appointments_serializer = serializers.BookingSerializer(appointments, many=True)
            for x in appointments_serializer.data:
                ## Pet Info
                pet_info = models.Pet.objects.get(pet_id = x['pet_id'])
                del x['pet_id']
                x['pet_info'] = serializers.PetSerializer(pet_info).data
                ## User Info
                user_info = models.User.objects.get(user_id = x['owner_id'])
                del x['owner_id']
                x['pet_owner'] = serializers.UserSerializerPartial(user_info).data
            return Response(appointments_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)