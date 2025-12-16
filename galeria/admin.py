from django.contrib import admin
from .models import Categoria, Obra, Contacto

class ObraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio')
    search_fields = ('titulo',)

# Registramos los modelos
admin.site.register(Categoria)
admin.site.register(Obra, ObraAdmin)
admin.site.register(Contacto) # Cumple con gestionar entidades