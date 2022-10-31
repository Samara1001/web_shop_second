from django.shortcuts import render, redirect
from .models import Electronic, Category
from rest_framework import viewsets
from .serializers import ElectronicSerializer, CategorySerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions




class ElectronicViewSet(viewsets.ModelViewSet):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer


class CategoryElectronicViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



