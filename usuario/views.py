from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm, iniciarSesion


# Vista para registro
class RegistroView(generic.FormView):
    template_name = 'usuario/registro.html'
    form_class = RegistroForm
    success_url = reverse_lazy('publicacion:inicio')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        usuario = form.save()
        return super().form_valid(form)

# Vista para inicio de sesión
class InicioView(auth_views.LoginView):
    template_name = 'usuario/inicio_sesion.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('publicacion:inicio')  # Corrige el error en el nombre del atributo

    def form_valid(self, form):
        remember_me = self.request.POST.get('remember_me', False)  # Checkbox "Recordarme"
        if remember_me:
            self.request.session.set_expiry(1209600)  # 2 semanas
        else:
            self.request.session.set_expiry(0)  # Cierra sesión al cerrar el navegador
        return super().form_valid(form)