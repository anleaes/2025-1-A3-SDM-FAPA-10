from django.shortcuts import render
from .models import Dieta
from rest_framework import viewsets
from .serializer import DietaSerializer

# Create your views here.

class DietaViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer
    
