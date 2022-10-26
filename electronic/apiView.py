from django.shortcuts import render, redirect
from .models import Electronic
from rest_framework import viewsets
from .serializers import ElectronicSerializer


class ElectronicViewSet(viewsets.ModelViewSet):
    queryset = Electronic.objects.all()
    serializer_class = ElectronicSerializer


