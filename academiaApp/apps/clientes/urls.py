from django.urls import path
from .views import cliente_list

urlpatterns = [
    path('', cliente_list, name='cliente_list'),
]