from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente
from .forms import ClienteForm


def create_cliente(request):
    template_name = "cliente/cadastroCliente.html"
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect("cliente:list_clientes")
    else:
        form = ClienteForm()
    return render(request, template_name, {"form": form})


def list_clientes(request):
    template_name = "cliente/list_clientes.html"
    clientes = Cliente.objects.all()
    context = {
        "clientes": clientes,  # Use plural para facilitar entendimento no template
    }
    return render(request, template_name, context)


def edit_cliente(request, id_cliente):
    template_name = "cliente/cadastroCliente.html"
    cliente = get_object_or_404(Cliente, id=id_cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect("cliente:list_clientes")
    else:
        form = ClienteForm(instance=cliente)
    return render(request, template_name, {"form": form})