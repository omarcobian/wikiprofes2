from django.shortcuts import render
from .models import Materia
from django.views import generic
from django.shortcuts import get_object_or_404
# Create your views here.

class ListaMateria(generic.ListView):
    template_name = 'materia/lista_materias.html'

    def get_queryset(self):
        return Materia.objects.order_by('nombre')


