from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            'materia', 'profesor', 'titulo', 'fecha', 'comentario',
            'dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento'
        ]
        widgets = {
            'materia': forms.Select(attrs={'class': 'form-select'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '80'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'maxlength': '2000'}),
            'dominio': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'puntualidad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'asistencia': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'dificultad': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
            'seguimiento': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'max': '5'}),
        }
