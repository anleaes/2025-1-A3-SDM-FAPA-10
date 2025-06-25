from django.urls import path
from .views import cliente_list, cliente_detail, cliente_create, cliente_delete, cliente_update

urlpatterns = [
    path('', cliente_list, name='cliente_list'),
    path('<int:pk>/', cliente_detail, name='cliente_detail'),
    path('novo/', cliente_create, name='cliente_create'),
    path('<int:pk>/editar/', cliente_update, name='cliente_update'),
    path('<int:pk>/deletar/', cliente_delete, name='cliente_delete'),
]