from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClientesForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def hello(request):
    return render(request, 'index.html')
@login_required
def clientes_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def clientes_new(request):
    form = ClientesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
    return render(request, 'clientes_form.html', {'form': form})
@login_required
def clientes_update(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClientesForm(request.POST or None, request.FILES or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('clientes_list')
    return render(request, 'clientes_form.html', {'form': form})
@login_required
def clientes_delete(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    form = ClientesForm(request.POST or None, request.FILES or None, instance=cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes_list')
    return render(request, 'clientes_delete_confirm.html', {'form': form})