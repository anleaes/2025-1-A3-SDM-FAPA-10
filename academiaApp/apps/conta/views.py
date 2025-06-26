from django.shortcuts import render
from .models import Conta
from rest_framework import viewsets
from .serializer import TreinoSerializer

# Create your views here.

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    
