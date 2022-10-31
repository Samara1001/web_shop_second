from django.urls import path, include
from rest_framework import routers
from . import apiView
from . import views



router = routers.DefaultRouter()
router.register(r'electronic', apiView.ElectronicViewSet)
router.register(r'category', apiView.CategoryElectronicViewSet)
router.register(r'users', apiView.UserViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('main', views.main, name='about'),
    path('<int:pk>/', views.ElectronicDetailView.as_view(), name='details'),
    path('create_page', views.create, name='create'),
    path('<int:pk>/update', views.ElectronicUpdateView.as_view(), name='update'),
    path('api', include(router.urls))



]
