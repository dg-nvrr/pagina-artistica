#!/usr/bin/env bash
# Salir si hay error
set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Recolectar archivos estáticos (CSS, JS, Imágenes del sistema)
python manage.py collectstatic --no-input

# Aplicar migraciones a la base de datos
python manage.py migrate