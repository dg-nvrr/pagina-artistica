# Portafolio Artista Visual - Marcela Navarro

Proyecto de gestión de arte y portafolio web.

## 📂 Estructura del Proyecto

* **`/frontend`**: Sitio web (`index.html`, `style.css`) con Bootstrap 5.
* **`/backend`**: Lógica administrativa en Python (`gestion.py`).
* **`/database`**: Archivos SQL (`script_galeria.sql`) con el modelo Relacional.

## 🗄️ Base de Datos
Se implementó un modelo relacional normalizado:
* **Tablas:** `Obras` y `Categorias` (Relación 1:N).
* **Script:** Incluye creación de tablas (DDL) e inserción de datos (DML).
* **Consultas:** Ejemplo de `INNER JOIN` para reportes.

## 🚀 Ejecución
1. Navegar a `/backend` y ejecutar `python gestion.py`.
2. Abrir `/frontend/index.html` para ver la galería.