from django.urls import path
from . import views

app_name = "personal"

urlpatterns = [
    path("adicionar/", views.novo_personal, name="cadastroPersonal"),
    path("", views.lista_personais, name="list_personais"),
    path("editar/<int:id_personal>/", views.editar_personal, name="editPersonal"),
    path("excluir/<int:id_personal>/", views.deletar_personal, name="delete_personal"),
]
