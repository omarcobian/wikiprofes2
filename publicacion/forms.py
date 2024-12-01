from django import forms
from .models import Publicacion

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['materia', 'profesor', 'usuario', 'titulo', 'fecha', 'comentario',
                  'dominio', 'puntualidad', 'asistencia', 'dificultad', 'seguimiento']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'comentario': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
