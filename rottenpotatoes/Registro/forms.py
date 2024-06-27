from django import forms
from .models import Pelicula


class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ["nombre", "genero", "duracion", "descripcion", "portada", "precio"]
        labels = {
            "descripcion": "Descripción",  # Cambia el label aquí
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
