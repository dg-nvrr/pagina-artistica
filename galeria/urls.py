from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear/', views.crear_obra, name='crear_obra'),
    path('editar/<int:id>/', views.editar_obra, name='editar_obra'),
    path('eliminar/<int:id>/', views.eliminar_obra, name='eliminar_obra'),
]