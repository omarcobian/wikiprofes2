from django.shortcuts import render
from .models import Profesor
from django.views import generic
from django.shortcuts import get_object_or_404

class ListaProfesor(generic.ListView):
    template_name = 'profesor/lista_profesores.html'

    def get_queryset(self):
        return Profesor.objects.order_by('nombre')


