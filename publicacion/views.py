from django.views import generic, View
from django.views.generic import CreateView
from django.shortcuts import render
from .models import Publicacion, Profesor, Materia
from .forms import PublicacionForm
from django.urls import reverse_lazy

class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]

class ProfesorView(generic.DetailView):
    model = Profesor
    template_name = 'publicacion/profesor.html'
    context_object_name = 'profesor'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profesor = self.get_object()
        context['publicacion_list'] = Publicacion.objects.filter(profesor=profesor)
        context['general_rating'] = profesor.get_general_rating()
        context['rubric_averages'] = profesor.get_rubric_averages()
        return context

class DetalleMateria(generic.ListView):
    template_name = 'publicacion/detalle_materia.html'

    def get_queryset(self):
        return Publicacion.objects.filter(materia_id=self.kwargs['materia_id'])

class SearchView(View):
    template_name = 'publicacion/busqueda.html'

    def get(self, request):
        query = request.GET.get('q')
        profesores = Profesor.objects.filter(nombre__icontains=query) if query else None
        materias = Materia.objects.filter(nombre__icontains=query) if query else None
        context = {
            'query': query,
            'profesores': profesores,
            'materias': materias,
        }
        return render(request, self.template_name, context)
    
class CrearPublicacionView(CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = 'publicacion/crear_publicacion.html'  # Cambia esto si tu archivo tiene otro nombre
    success_url = reverse_lazy('index')  # Cambia este nombre según tu URL definida

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['materias'] = self.get_materias()
        context['profesores'] = self.get_profesores()
        return context

    def get_materias(self):
        """Retorna todas las materias disponibles"""
        return Materia.objects.all()

    def get_profesores(self):
        """Retorna todos los profesores disponibles"""
        return Profesor.objects.all()
