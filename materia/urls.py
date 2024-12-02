from django.urls import path
from . import views

app_name = 'materia'

urlpatterns = [
    path('materias/', views.ListaMateria.as_view(), name='lista_materias'),
]
