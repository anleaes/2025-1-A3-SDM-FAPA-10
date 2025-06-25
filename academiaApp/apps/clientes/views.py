from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Cliente
from .forms import UserForm, ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detail.html', {'cliente': cliente})

def cliente_create(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if user_form.is_valid() and cliente_form.is_valid():
            user = user_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.user = user
            cliente.save()
            return redirect('cliente_list')
    else:
        user_form = UserForm()
        cliente_form = ClienteForm()
    return render(request, 'clientes/form.html', {
        'user_form': user_form,
        'cliente_form': cliente_form,
        'acao': 'Criar'
    })

def cliente_update(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    user = cliente.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        cliente_form = ClienteForm(request.POST, instance=cliente)
        if user_form.is_valid() and cliente_form.is_valid():
            user_form.save()
            cliente_form.save()
            return redirect('cliente_list')
    else:
        user_form = UserForm(instance=user)
        cliente_form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form.html', {
        'user_form': user_form,
        'cliente_form': cliente_form,
        'acao': 'Editar'
    })

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.user.delete()  # apaga o user junto
        return redirect('cliente_list')
    return render(request, 'clientes/confirm_delete.html', {'cliente': cliente})