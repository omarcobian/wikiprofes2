from django.shortcuts import render
from django.views import generic
from .models import Publicacion
from .forms import PublicacionForm

# Create your views here.
class PublicacionView(generic.ListView):
    template_name = 'publicacion/index.html'

    def get_queryset(self):
        return Publicacion.objects.order_by('-fecha')[:5]
    
    
class crearPublicacion(generic.FormView):
    template_name = 'publicacion/crear_publicacion.html'
    def crear_publicacion(request):
        if request.method == "POST":
            form = PublicacionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('nombre_de_la_vista_post_creacion')  # Redirige a otra vista después de guardar
        else:
            form = PublicacionForm()
        return render(request, 'crear_publicacion.html', {'form': form})

class indexView(generic.TemplateView):
    template_name = 'usuario/inicio.html'