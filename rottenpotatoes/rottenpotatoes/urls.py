from django.contrib import admin
from django.urls import path
from Registro import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.base, name="base"),
    path("contacto/", views.contacto, name="contacto"),
    path("next/", views.next, name="next"),
    path("tienda/", views.tienda, name="tienda"),
    path("who/", views.who, name="who"),
    path("Registro/", views.registro, name="registro"),

    path("peliculas/", views.PeliculaList.as_view(), name="pelicula_list"),
    path(
        "pelicula/registrar/", views.PeliculaCreate.as_view(), name="registrar_pelicula"
    ),
    path(
        "pelicula/<int:pk>/editar/",
        views.PeliculaUpdate.as_view(),
        name="pelicula_update",
    ),
    path(
        "pelicula/<int:pk>/borrar/",
        views.PeliculaDelete.as_view(),
        name="pelicula_borrar",
    ),
    path("login/", views.login_view, name="login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
