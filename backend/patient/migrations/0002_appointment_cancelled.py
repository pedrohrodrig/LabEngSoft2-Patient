# Generated by Django 5.0.4 on 2024-04-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="cancelled",
            field=models.BooleanField(default=False),
        ),
    ]
