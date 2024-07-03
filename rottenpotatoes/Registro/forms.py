from django import forms
from .models import Pelicula
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["nombre", "genero", "duracion", "descripcion", "portada", "precio"]
        labels = {
            "descripcion": "Descripción",
        }
        widgets = {
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["descripcion"].widget.attrs.update(
            {
                "class": "form-control",
                "rows": 3,
                "id": "id_descripcion",
                "placeholder": "Ingrese la descripción aquí",  # Ejemplo de placeholder
            }
        )
        self.fields["descripcion"].label = "Descripción"
        self.fields["descripcion"].widget.attrs.update(
            {"class": "label-descripcion"}
        )  # Aplica la clase CSS al label


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
