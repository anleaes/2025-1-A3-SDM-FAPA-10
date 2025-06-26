from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'conta'

router = routers.DefaultRouter()
router.register('', views.ContaViewSet, basename='conta')

urlpatterns = [
    path('', include(router.urls) )
]