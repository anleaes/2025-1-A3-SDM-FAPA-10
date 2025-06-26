from django.shortcuts import render, redirect
from .models import Personal
from .forms import PersonalForm

# Create your views here.


def novo_personal(request):
    if request.method == "POST":
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/personal/lista/")
    else:
        form = PersonalForm()
    return render(request, "personal/cadastroPersonal.html", {"form": form})


def lista_personais(request):
    dados = Personal.objects.all()
    return render(request, "personal/list_personais.html", {"personal": dados})


def editar_personal(request, id):
    personal = Personal.objects.get(id=id)
    if request.method == "POST":
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect("/personal/lista/")
    else:
        form = PersonalForm(instance=personal)
    return render(request, "personal/editarPersonal.html", {"form": form})


def deletar_personal(request, id):
    personal = Personal.objects.get(id=id)
    personal.delete()
    return redirect("/personal/lista/")