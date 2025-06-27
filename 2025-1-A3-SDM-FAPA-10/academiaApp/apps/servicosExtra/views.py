from django.shortcuts import render
from .models import ServicosExtra
from rest_framework import viewsets
from .serializer import ServicosExtraSerializer

# Create your views here.

class ServicosExtraViewSet(viewsets.ModelViewSet):
    queryset = ServicosExtra.objects.all()
    serializer_class = ServicosExtraSerializer
    
