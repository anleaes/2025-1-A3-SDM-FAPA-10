from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'personal'

router = routers.DefaultRouter()
router.register('', views.PersonalViewSet, basename='personal')

urlpatterns = [
    path('', include(router.urls) )
]