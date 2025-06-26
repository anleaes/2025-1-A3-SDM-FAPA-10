from django.shortcuts import render
from .models import Alimento
from rest_framework import viewsets
from .serializer import AlimentoSerializer

# Create your views here.

class AlimentoViewSet(viewsets.ModelViewSet):
    queryset = Alimento.objects.all()
    serializer_class = AlimentoSerializer
    
