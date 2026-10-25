WEB PERSONAL - DJANGO
=====================

Este proyecto adapta el frontend entregado por el docente a Django.

1. Abrir la carpeta "webpersonal" en PyCharm.

2. Crear/activar un entorno virtual (recomendado).

3. Instalar Django:
   pip install -r requirements.txt

4. Crear las migraciones:
   python manage.py makemigrations
   python manage.py migrate

5. Crear el usuario administrador:
   python manage.py createsuperuser

6. Ejecutar:
   python manage.py runserver

7. Entrar al administrador:
   http://127.0.0.1:8000/admin/

8. En "Persona", crear UN SOLO registro con:
   - Nombres
   - Apellidos
   - Dirección
   - Teléfono
   - Título académico
   - Biografía
   - Correo electrónico
   - Dedicación

9. En "Proyectos", crear los proyectos del portafolio.
   En "Imagen" se puede escribir, por ejemplo:
   img/home-bg.jpg
   img/about-bg.jpg
   img/portfolio-bg.jpg

RUTAS:
   /              -> Portada
   /acerca-de/    -> Acerca de
   /portafolio/  -> Portafolio
   /contacto/    -> Contacto
   /admin/       -> Administrador

IMPORTANTE:
Los datos que aparecen en la página se leen de la base de datos mediante los
modelos Persona y Proyecto. No están escritos directamente en las plantillas.
