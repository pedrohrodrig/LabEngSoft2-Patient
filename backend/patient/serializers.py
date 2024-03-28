from rest_framework import serializers

from .models import Appointment, Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = Appointment
        fields = ["id_user_professional", "datetime", "is_online"]
