from django.contrib import admin
from django.urls import path, include  # Importar 'include'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("Registro.urls")),  # Incluir las URLs de la aplicación 'Registro'
]
