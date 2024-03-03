from django.db import models

class Patient(models.Model):
    full_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=True, default="")
    document = document = models.CharField(max_length=15, unique=True, blank=True, null=True)

    class Meta:
        db_table = "patient"