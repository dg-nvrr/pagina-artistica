from django.db import models

# --- Req 2: Entidad no relacionada (Para guardar mensajes del formulario) ---
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.nombre}"

# --- Req 3: Entidades Relacionadas (Categoría y Obra) ---
class Categoria(models.Model):
    nombre_tecnica = models.CharField(max_length=50) # Ej: "Óleo sobre lienzo", "Óleo sobre madera"

    def __str__(self):
        return self.nombre_tecnica

class Obra(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True) # Agregamos descripción
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='obras/', null=True, blank=True) # Para subir fotos reales
    
    # Relación Uno a Muchos (Una categoría tiene muchas obras)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} (${self.precio})"