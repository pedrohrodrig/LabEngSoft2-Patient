from datetime import datetime

from cpf_field.models import CPFField
from django.db import models


class Patient(models.Model):
    id_user = models.PositiveIntegerField(unique=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    birth_date = models.DateField(blank=False, null=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    cpf = CPFField("cpf")
    address = models.CharField(max_length=255, null=False, blank=False)
    gender = models.CharField(
        max_length=1, blank=False, null=False, choices=(("F", "Female"), ("M", "Male"), ("O", "Others"))
    )

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        db_table = "patient"


class AppointmentStatus(models.IntegerChoices):
    SCHEDULED = 1, "Agendada"
    DONE = 2, "Finalizada"
    CANCELLED = 3, "Cancelada"


class Appointment(models.Model):
    id_user_professional = models.PositiveIntegerField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    datetime = models.DateTimeField()
    is_online = models.BooleanField()
    cancelled = models.BooleanField(default=False)

    @property
    def status(self):
        if self.cancelled:
            return AppointmentStatus.CANCELLED

        if datetime.now() > self.datetime:
            return AppointmentStatus.DONE

        return AppointmentStatus.SCHEDULED
