from django.contrib import admin
from .models import Persona, Proyecto


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        "nombres",
        "apellidos",
        "correo_electronico",
        "dedicacion",
    )

    fieldsets = (
        ("Datos personales", {
            "fields": (
                "nombres",
                "apellidos",
                "direccion",
                "telefono",
            )
        }),
        ("Información académica y profesional", {
            "fields": (
                "titulo_academico",
                "dedicacion",
                "biografia",
                "correo_electronico",
            )
        }),
    )

    def has_add_permission(self, request):
        # La consigna solicita un solo registro de Persona.
        return not Persona.objects.exists()


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "enlace")
    search_fields = ("titulo", "descripcion")
