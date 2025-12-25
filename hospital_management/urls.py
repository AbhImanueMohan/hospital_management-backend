from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/auth/", include("accounts.urls")),
    path("api/doctors/", include("doctors.urls")),
    path("api/patient/", include("patients.urls")),
    path("api/appointments/", include("appointments.urls")),
]

# React frontend (must be LAST)
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
