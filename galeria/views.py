from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required # EL CANDADO
from .models import Obra
from .forms import ObraForm

# --- Vista Pública (Cualquiera puede verla) ---
def inicio(request):
    obras = Obra.objects.all()
    return render(request, 'index.html', {'obras': obras})

# --- Vistas Privadas (Solo Staff/Admin puede entrar) ---

@staff_member_required(login_url='admin:login') # Si no es admin, lo manda al login
def crear_obra(request):
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
    obra = get_object_or_404(Obra, id=id)
    obra.delete()
    return redirect('inicio')