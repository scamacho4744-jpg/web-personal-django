from django.db import models


class Persona(models.Model):
    nombres = models.CharField("Nombres", max_length=100)
    apellidos = models.CharField("Apellidos", max_length=100)
    direccion = models.CharField("Dirección", max_length=200)
    telefono = models.CharField("Teléfono", max_length=30)
    titulo_academico = models.CharField("Título académico", max_length=200)
    biografia = models.TextField("Biografía")
    correo_electronico = models.EmailField("Correo electrónico")
    dedicacion = models.CharField("Dedicación", max_length=200)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Persona"

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"


class Proyecto(models.Model):
    titulo = models.CharField("Título", max_length=150)
    descripcion = models.TextField("Descripción")
    enlace = models.URLField("Enlace", blank=True)
    imagen = models.CharField(
        "Imagen (ruta dentro de static)",
        max_length=200,
        blank=True,
        help_text="Ejemplo: img/home-bg.jpg",
    )

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ["-id"]

    def __str__(self):
        return self.titulo
