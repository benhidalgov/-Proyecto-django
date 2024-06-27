from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracion = models.IntegerField()
    descripcion = models.TextField()
    portada = models.ImageField(upload_to="portadas/")
    precio = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(999999)]
    )

    def __str__(self):
        return self.nombre


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            # Redirige a donde desees después del inicio de sesión exitoso
            return redirect(
                "base"
            )  # Cambia 'base' por la URL a la que deseas redirigir
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "login.html")


def registro_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Cuenta creada para {username}!")
            login(request, user)
            return redirect("base")
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})
