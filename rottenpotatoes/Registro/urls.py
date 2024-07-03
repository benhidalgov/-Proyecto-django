from django.urls import path, reverse_lazy
from Registro import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

urlpatterns = [
    path("", views.base, name="base"),
    path("contacto/", views.contacto, name="contacto"),
    path("next/", views.next, name="next"),
    path("tienda/", views.tienda, name="tienda"),
    path("who/", views.who, name="who"),
    path("Registro/", views.registro, name="Registro"),
    path("peliculas/", views.PeliculaList.as_view(), name="pelicula_list"),
    path("pelicula/registrar/", lambda request: redirect('admin:Registro_pelicula_add'), name="registrar_pelicula"),
    path("pelicula/<int:pk>/editar/", views.PeliculaUpdate.as_view(), name="pelicula_update"),
    path("pelicula/<int:pk>/borrar/", views.PeliculaDelete.as_view(), name="pelicula_borrar"),
    path("login/", views.login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
