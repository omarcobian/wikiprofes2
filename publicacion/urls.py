from django.urls import path
from . import views


app_name = 'publicacion'
urlpatterns = [
    path('publicacion', views.PublicacionView.as_view(), name='index'), #'/'
    path('crear_publicacion', views.crearPublicacion.as_view(), name='crearPubli'),
    path('', views.indexView.as_view(), name='inicio'),
]
