from django.views import generic, View
from django.shortcuts import render
from .models import Publicacion, Profesor, Materia

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
