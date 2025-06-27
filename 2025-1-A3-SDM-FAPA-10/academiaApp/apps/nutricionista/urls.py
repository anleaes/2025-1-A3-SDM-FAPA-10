from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'nutricionista'

router = routers.DefaultRouter()
router.register('', views.NutricionistaViewSet, basename='nutricionista')

urlpatterns = [
    path('', include(router.urls) )
]