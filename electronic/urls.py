from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='about'),
]
