from django.db import models

# Modelo para las Categorías (Pintura, Orfebrería, etc.)
class Categoria(models.Model):
    nombre_tecnica = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tecnica

# Modelo para las Obras de Arte
class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    precio = models.IntegerField()
    # Relación: Una obra pertenece a una categoría
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} (${self.precio})"