from django.shortcuts import render
from .models import Personal
from rest_framework import viewsets
from .serializer import PersonalSerializer

# Create your views here.

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    
