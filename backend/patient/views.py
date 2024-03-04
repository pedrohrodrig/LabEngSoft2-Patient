from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Patient
from .serializers import PatientSerializer


class PatientView(ModelViewSet):
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

    def list_all(self, request):
        patient_list = Patient.objects.all()

        if not patient_list:
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = PatientSerializer(patient_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
