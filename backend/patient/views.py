from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Appointment, Patient
from .permissions import AllowPostOnlyPermission
from .serializers import AppointmentSerializer, PatientSerializer


class PatientView(ModelViewSet):
    permission_classes = [
        AllowPostOnlyPermission,
    ]

    def create(self, request):
        serializer = PatientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        patient = Patient.objects.create(**serializer.validated_data)
        patient_serialized = PatientSerializer(patient)

        return Response(patient_serialized.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        patient = Patient.objects.filter(pk=pk).first()

        if not patient:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_from_logged_user(self, request):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        patient = Patient.objects.filter(id_user=user.id).first()
        if not patient:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PatientSerializer(patient)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_all(self, request):
        patient_list = Patient.objects.all()

        if not patient_list:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = PatientSerializer(patient_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_patients_from_professional(self, request, id_user_professional):
        professional_patients = Patient.objects.filter(
            appointments__id_user_professional=id_user_professional
        ).distinct()
        if not professional_patients:
            return Response(status=status.HTTP_204_NO_CONTENT)

        professional_patients_serialized = PatientSerializer(professional_patients, many=True)

        return Response(professional_patients_serialized.data, status=status.HTTP_200_OK)


class AppointmentView(ModelViewSet):
    def retrieve(self, request, pk):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        appointment = Appointment.objects.get(pk=pk)
        if not appointment:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = AppointmentSerializer(appointment)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list_all_from_user(self, request):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        appointments = Appointment.objects.filter(patient__id_user=user.id)

        serializer = AppointmentSerializer(appointments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        patient = Patient.objects.get(id_user=user.id)
        if not patient:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = AppointmentSerializer({"patient": {**patient}, **request.data})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        appointment = Appointment.objects.create(**serializer.validated_data)
        appointment_serialized = AppointmentSerializer(appointment.data)

        return Response(appointment_serialized.data, status=status.HTTP_201_CREATED)

    def cancel(self, request, pk):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        appointment = Appointment.objects.get(id=pk)
        appointment.cancelled = True
        appointment.save()

        return Response(status=status.HTTP_200_OK)

    def list_from_professional_id(self, request, id_user_professional):
        user = request.user
        if not user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        appointment = Appointment.objects.filter(id_user_professional=id_user_professional)
        if not appointment:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = AppointmentSerializer(appointment, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
