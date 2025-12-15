# Portafolio Artista Visual - Marcela Navarro (Django Version)

Plataforma web de gestión de arte y portafolio digital, migrada a una arquitectura MVT (Modelo-Vista-Template) con Django.

## 🚀 Tecnologías
* **Backend:** Python 3, Django 5.
* **Frontend:** HTML5, CSS3, Bootstrap 5.
* **Seguridad:** Gestión de variables de entorno con `python-dotenv`.
* **Base de Datos:** SQLite (Desarrollo).

## 📂 Estructura del Proyecto
* **`/core`**: Configuración principal del proyecto (`settings.py`, `urls.py`).
* **`/galeria`**: Aplicación principal. Contiene:
    * `models.py`: Modelos de base de datos (Obras, Categorías).
    * `views.py`: Lógica de presentación.
    * `admin.py`: Configuración del panel administrativo.
* **`/frontend`**: (Deprecado) Archivos estáticos originales antes de la migración.

## 🛠️ Instalación y Ejecución

1. **Clonar y preparar entorno:**
   ```bash
   # Activar entorno virtual (Windows)
   source venv/Scripts/activate
   
   # Instalar dependencias
   pip install django python-dotenv