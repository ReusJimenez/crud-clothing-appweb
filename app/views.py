from django.shortcuts import render, redirect
from app.models import Prenda
from app.forms import PrendaForm

# Create your views here.
def listar(request):
    prendas = Prenda.objects.all()
    contexto = {'prendas': prendas}
    return render(request, 'listar.html', contexto)

def agregar(request):
    if request.method == "POST":
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('listar')
    else:
        form = PrendaForm()
    contexto = {'form': form}
    return render(request, 'agregar.html', contexto)

def editar(request, prenda_id):
    prenda = Prenda.objects.get(id=prenda_id)
    if request.method == "POST":
        form = PrendaForm(request.POST, instance=prenda)
        if form.is_valid():
            form.save(commit=True)
            return redirect('listar')
    else:
        form = PrendaForm(instance=prenda)
    contexto = {'form': form}
    return render(request, 'editar.html', contexto)

def eliminar(request, prenda_id):
    prenda = Prenda.objects.get(id=prenda_id)
    prenda.delete()
    return redirect('listar')   
