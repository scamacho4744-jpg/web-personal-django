from django.shortcuts import render
from .models import Persona, Proyecto


def datos_comunes():
    return {
        "persona": Persona.objects.first(),
    }


def inicio(request):
    context = datos_comunes()
    return render(request, "index.html", context)


def acerca_de(request):
    context = datos_comunes()
    return render(request, "about.html", context)


def portafolio(request):
    context = datos_comunes()
    context["proyectos"] = Proyecto.objects.all()
    return render(request, "portfolio.html", context)


def contacto(request):
    context = datos_comunes()
    return render(request, "contact.html", context)
