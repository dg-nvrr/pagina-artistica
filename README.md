# 🎨 Portafolio Artista Visual - Marcela Navarro

Plataforma web profesional desarrollada en Django para la gestión y exhibición de obras de arte (Óleo sobre lienzo, Orfebrería y Mixta).

## ✨ Características Principales

* **Galería Responsiva:** Diseño "Masonry" adaptativo que mantiene la proporción estética de las obras en móviles, tablets y escritorio.
* **Gestión de Contenido (CRUD):** Sistema completo para Agregar, Leer, Editar y Eliminar obras directamente desde la interfaz web.
* **Seguridad RBAC:** * Los botones de edición y gestión son **invisibles** para visitantes públicos.
    * Protección a nivel de servidor (Backend) que impide accesos no autorizados a las URLs de gestión.
    * Vista exclusiva de administrador con alertas visuales.
* **Optimización de Imágenes:** Procesamiento automático de miniaturas y ajuste de relación de aspecto (4:5).

## 🚀 Tecnologías Utilizadas

* **Backend:** Python 3.12, Django 5.0
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Base de Datos:** SQLite3 (Entorno de desarrollo)
* **Seguridad:** `python-dotenv` para variables de entorno.

## 🛠️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/dg-nvrr/pagina-artistica](https://github.com/dg-nvrr/pagina-artistica)
    cd portafolio-artista
    ```

2.  **Crear y activar entorno virtual:**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar variables de entorno:**
    Crea un archivo `.env` en la raíz y agrega:
    ```env
    SECRET_KEY='tu_clave_secreta_django'
    DEBUG=True
    ```

5.  **Migrar y crear superusuario:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

6.  **Ejecutar servidor:**
    ```bash
    python manage.py runserver
    ```

## 👤 Autor
Desarrollado para Marcela Navarro por Dg-nvrr