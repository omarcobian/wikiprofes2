from django.urls import path
from . import views

app_name = 'usuario'
urlpatterns = [
    path('registro', views.RegistroView.as_view(), name='registro'), #localhost/registro
    path('inicio', views.InicioView.as_view(), name='inicio'), #localhost/inicio
]