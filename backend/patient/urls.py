from django.urls import path

from .views import AppointmentView, PatientView

urlpatterns = [
    path("patient/", PatientView.as_view(actions={"post": "create", "get": "list_all"})),
    path("patient/<int:pk>/", PatientView.as_view(actions={"get": "retrieve"})),
    path("patient_from_logged_user/", PatientView.as_view(actions={"get": "get_from_logged_user"})),
    path("appointment/", AppointmentView.as_view(actions={"post": "create", "get": "list_all_from_user"})),
    path("appointment/<int:pk>/", AppointmentView.as_view(actions={"get": "retrieve"})),
]
