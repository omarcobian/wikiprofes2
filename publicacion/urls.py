from django.urls import path
from . import views


app_name = 'publicacion'
urlpatterns = [
    path('publicacion', views.PublicacionView.as_view(), name='index'), #'/'
    path('materia/<int:materia_id>/', views.DetalleMateria.as_view(), name='detalle_materia'),
    path('profesor/<int:pk>/', views.ProfesorView.as_view(), name='profesor'),
    path('crear/', views.CrearPublicacionView.as_view(), name='crear_publicacion'),
    path('search/', views.SearchView.as_view(), name='search')
]
