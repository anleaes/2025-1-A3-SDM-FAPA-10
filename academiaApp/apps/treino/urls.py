from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'treino'

router = routers.DefaultRouter()
router.register('', views.TreinoViewSet, basename='treino')

urlpatterns = [
    path('', include(router.urls) )
]