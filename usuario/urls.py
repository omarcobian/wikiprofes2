from django.urls import path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

app_name = 'usuario'

# Función directa para cerrar sesión
def logout_and_redirect(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('usuario:inicio')  # Redirige al usuario a 'usuario:inicio'

urlpatterns = [
    path('registro', views.RegistroView.as_view(), name='registro'),  # localhost/registro
    path('inicio', views.InicioView.as_view(), name='inicio'),        # localhost/inicio
    path('logout/', logout_and_redirect, name='logout'),              # localhost/logout
]
