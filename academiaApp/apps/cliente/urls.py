from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('novo/', views.create_cliente, name='create_cliente'),
    path('lista/', views.list_clientes, name='list_clientes'),
    path('editar/<int:id_cliente>/', views.edit_cliente, name='edit_cliente'),
    path('deletar/<int:id_cliente>/', views.delete_cliente, name='delete_cliente'),
    path('buscar/', views.search_cliente, name='search_cliente'),
]