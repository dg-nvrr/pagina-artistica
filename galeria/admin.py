from django.contrib import admin
from .models import Categoria, Obra

# Registramos los modelos para que aparezcan en el panel
admin.site.register(Categoria)
admin.site.register(Obra)