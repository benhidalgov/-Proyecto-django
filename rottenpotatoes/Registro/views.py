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


class PeliculaList(ListView):
    model = Pelicula
    template_name = "pelicula_list.html"


class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "pelicula_form.html"
    success_url = reverse_lazy("pelicula_list")

    def form_valid(self, form):
        pelicula = form.save(commit=False)
        pelicula.save()
        return super().form_valid(form)


class PeliculaUpdate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "pelicula_form.html"
    success_url = reverse_lazy("pelicula_list")


class PeliculaDelete(DeleteView):
    model = Pelicula
    template_name = "pelicula_confirm_delete.html"
    success_url = reverse_lazy("pelicula_list")


@login_required
def animalrandom(request):
    return render(request, "animalrandom.html")


def base(request):
    return render(request, "base.html")


def contacto(request):
    return render(request, "contacto.html")


def next(request):
    return render(request, "next.html")


def tienda(request):
    return render(request, "tienda.html")


def who(request):
    return render(request, "who.html")


def registro(request):
    if request.method == "POST":
        try:
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            password_confirm = request.POST["password_confirm"]

            # Validación básica de contraseñas
            if password != password_confirm:
                messages.error(request, "Las contraseñas no coinciden.")
                return redirect("registro")

            # Crear usuario
            user = User.objects.create_user(
                username=username, email=email, password=password
            )
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("base")  # Redirigir al inicio

        except Exception as e:
            messages.error(request, f"Error al registrar usuario: {e}")
            return redirect("registro")

    return render(request, "registro.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next", "")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            else:
                return redirect("base")
        else:
            return render(
                request,
                "login.html",
                {"next": next_url, "error_message": "Credenciales inválidas"},
            )
    else:
        next_url = request.GET.get("next", "")
        return render(request, "login.html", {"next": next_url})


def pelicula_borrar(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == "POST":
        pelicula.delete()
        return redirect("pelicula_list")
    return render(request, "pelicula_confirm_delete.html", {"object": pelicula})


def pelicula_list(request):
    peliculas = Pelicula.objects.all()
    return render(request, "pelicula_list.html", {"object_list": peliculas})


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
