from django.urls import path
from . import views

app_name = 'profesor'

urlpatterns = [
    path("profesores/", views.ListaProfesor.as_view(), name="lista_profesores"),
]
