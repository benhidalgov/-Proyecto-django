from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from .models import Pelicula
from .forms import PeliculaForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from .forms import RegistroForm
from django.middleware.csrf import get_token
from django.contrib.auth import logout
from django.shortcuts import redirect

from django.contrib.auth import logout
from django.shortcuts import redirect
import logging

logger = logging.getLogger(__name__)


def logout_view(request):
    logger.info("Intento de cierre de sesión.")
    logout(request)
    logger.info("Sesión cerrada exitosamente.")
    return redirect("base")


class PeliculaList(ListView):
    model = Pelicula
    template_name = "pelicula_list.html"


class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "pelicula_form.html"

    def form_valid(self, form):
        self.object = form.save()
        return redirect("admin:Registro_pelicula_add")


class PeliculaUpdate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "pelicula_form.html"
    success_url = reverse_lazy("pelicula_list")


class PeliculaDelete(DeleteView):
    model = Pelicula
    template_name = "pelicula_confirm_delete.html"
    success_url = reverse_lazy("pelicula_list")


def base(request):
    return render(request, "base.html")


def contacto(request):
    return render(request, "contacto.html")


def tienda(request):
    return render(request, "tienda.html")


def who(request):
    return render(request, "who.html")


def registro(request):
    if (
        request.method == "POST"
        and request.headers.get("x-requested-with") == "XMLHttpRequest"
    ):
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        errors = []

        if not username or not email or not password or not password_confirm:
            errors.append("Todos los campos son obligatorios.")

        if password != password_confirm:
            errors.append("Las contraseñas no coinciden.")

        if User.objects.filter(username=username).exists():
            errors.append("El nombre de usuario ya está en uso.")

        if User.objects.filter(email=email).exists():
            errors.append("El correo electrónico ya está en uso.")

        if errors:
            return JsonResponse({"success": False, "errors": errors})

        user = User.objects.create_user(
            username=username, email=email, password=password
        )
        user = authenticate(username=username, password=password)
        login(request, user)

        return JsonResponse({"success": True, "username": username, "email": email})

    # Añadir un token CSRF en la respuesta
    csrf_token = get_token(request)
    return render(request, "registro.html", {"csrf_token": csrf_token})


def login_view(request):
    if request.method == "POST":
        # Verificar si es una solicitud AJAX
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"success": True, "username": username})
            else:
                return JsonResponse(
                    {"success": False, "error": "Credenciales inválidas"}
                )

        # Si no es AJAX, manejar como una solicitud normal de formularios HTML
        else:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireccionar después del inicio de sesión
                return redirect(
                    "tienda"
                )  # Cambia "tienda" por la URL a la que quieres redirigir

            # Si la autenticación falla, mostrar el formulario de inicio de sesión nuevamente
            context = {"csrf_token": get_token(request)}
            return render(request, "login.html", context)

    # Si es una solicitud GET, mostrar el formulario de inicio de sesión
    context = {"csrf_token": get_token(request)}
    return render(request, "login.html", context)


def pelicula_borrar(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        pelicula.delete()
        return redirect("pelicula_list")
    return render(request, "pelicula_confirm_delete.html", {"object": pelicula})


def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render(request, "tu_template.html", {"peliculas": peliculas})


def pelicula_update(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            return redirect("pelicula_list")
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, "pelicula_form.html", {"form": form})


def pelicula_borrar(request, nombre):
    pelicula = get_object_or_404(Pelicula, nombre=nombre)
    if request.method == "POST":
        pelicula.delete()
        return redirect("pelicula_list")
    return render(request, "pelicula_borrar.html", {"object": pelicula})


def logout_view(request):
    logout(request)
    return redirect("base")


def next(request):
    # Lógica de tu vista 'next'
    return render(request, "base.html")


def tienda(request):
    peliculas = Pelicula.objects.all()
    return render(request, "tienda.html", {"peliculas": peliculas})
