from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'alimento'

router = routers.DefaultRouter()
router.register('', views.AlimentoViewSet, basename='alimento')

urlpatterns = [
    path('', include(router.urls) )
]