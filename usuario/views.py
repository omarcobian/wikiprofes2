from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib.auth import views

# Create your views here.
class RegistroView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('publicacion:index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = form.save()
        #el usuario sera utilizado para el login del futuro
        return super().form_valid(form)
    
class InicioView(views.LoginView):
    template_name ='usuario/inicio_sesion.html'
    redirect_authenticated_user = True
    nex_page = 'publicacion:index'