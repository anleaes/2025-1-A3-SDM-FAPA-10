from django.shortcuts import render
from .models import HomePage
from rest_framework import viewsets
from .serializer import HomePageSerializer

# Create your views here.

class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    
