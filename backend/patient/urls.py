from django.urls import path

from .views import PatientView

urlpatterns = [
    path("patient/", PatientView.as_view(actions={"post": "create"})),
    path("patient/<int:pk>/", PatientView.as_view(actions={"get": "retrieve"})),
]
