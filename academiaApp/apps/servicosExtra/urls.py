from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'servicosExtra'

router = routers.DefaultRouter()
router.register('', views.ServicosExtraViewSet, basename='servicosExtra')

urlpatterns = [
    path('', include(router.urls) )
]