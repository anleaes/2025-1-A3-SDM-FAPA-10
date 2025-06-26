from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'dieta'

router = routers.DefaultRouter()
router.register('', views.DietaViewSet, basename='dieta')

urlpatterns = [
    path('', include(router.urls) )
]