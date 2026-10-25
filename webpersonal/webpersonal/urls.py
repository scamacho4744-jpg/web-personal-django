from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.inicio, name="inicio"),
    path("acerca-de/", views.acerca_de, name="acerca_de"),
    path("portafolio/", views.portafolio, name="portafolio"),
    path("contacto/", views.contacto, name="contacto"),
]
