from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Obra
from .forms import ObraForm

def inicio(request):
    """
    Vista pública principal.
    Recupera todas las obras de la base de datos y las renderiza
    en la plantilla pública.
    """
    obras = Obra.objects.all()
    return render(request, 'index.html', {'obras': obras})

@staff_member_required(login_url='admin:login')
def crear_obra(request):
    """
    Vista de gestión (Create).
    Permite a los administradores subir una nueva obra.
    Valida el formulario y guarda la imagen adjunta.
    """
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ObraForm()
    return render(request, 'form_obra.html', {'form': form, 'titulo': 'Nueva Obra'})

@staff_member_required(login_url='admin:login')
def editar_obra(request, id):
    """
    Vista protegida para edición (Update).
    Recupera una obra por su ID y carga el formulario con sus datos actuales.
    """
    obra = get_object_or_404(Obra, id=id)
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = ObraForm(instance=obra)
    return render(request, 'form_obra.html', {'form': form, 'titulo': 'Editar Obra'})

@staff_member_required(login_url='admin:login')
def eliminar_obra(request, id):
    """
    Vista protegida de eliminación (Delete).
    Borra permanentemente el registro de la obra seleccionada.
    """
    obra = get_object_or_404(Obra, id=id)
    obra.delete()
    return redirect('inicio')