from django.urls import path, include
from rest_framework import routers
from . import apiView
from . import views



router = routers.DefaultRouter()
router.register(r'electronic', apiView.ElectronicViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='about'),
    path('main', views.main, name='about'),
    path('', include(routers.urls))


]
