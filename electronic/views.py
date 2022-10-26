from django.shortcuts import render
from .models import Electronic, Category


def index(requests):
    return render(requests)


def main(request):
    return render(request)


def electronic(request):
    return render(request)


def category(request):
    return render(request)