from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Patient
from .serializers import PatientSerializer

class PatientView(ModelViewSet):

    def create_patient(self, request):
        serializer = PatientSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        patient = Patient.objects.create(**serializer.validated_data)
        patient_serialized = PatientSerializer(patient)

        return Response(patient_serialized.data, status=status.HTTP_201_CREATED)