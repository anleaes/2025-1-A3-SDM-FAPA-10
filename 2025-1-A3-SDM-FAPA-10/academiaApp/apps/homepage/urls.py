from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'homepage'

router = routers.DefaultRouter()
router.register('', views.HomePageViewSet, basename='homepage')

urlpatterns = [
    path('', include(router.urls) )
]