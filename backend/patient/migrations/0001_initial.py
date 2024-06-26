# Generated by Django 5.0.3 on 2024-04-03 03:05

import cpf_field.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("id_user", models.PositiveIntegerField(unique=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("phone_number", models.CharField(blank=True, default="", max_length=15)),
                ("cpf", cpf_field.models.CPFField(max_length=14, verbose_name="cpf")),
                ("address", models.CharField(max_length=255)),
                ("gender", models.CharField(choices=[("F", "Female"), ("M", "Male"), ("O", "Others")], max_length=1)),
            ],
            options={
                "db_table": "patient",
            },
        ),
        migrations.CreateModel(
            name="Appointment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("id_user_professional", models.PositiveIntegerField()),
                ("datetime", models.DateTimeField()),
                ("is_online", models.BooleanField()),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="appointments", to="patient.patient"
                    ),
                ),
            ],
        ),
    ]
