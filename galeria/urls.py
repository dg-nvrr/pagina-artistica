from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Asegúrate de tener una vista llamada 'index' en views.py
]