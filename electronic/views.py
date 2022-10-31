from django.shortcuts import render
from .models import Electronic, Category


def index(requests):
    electronic = Electronic.objects.all()
    return render(requests, 'electronic/index.html', {"data": electronic})


def main(request):
    return render(request)


def electronic(request):
    return render(request)


def category(request):
    return render(request)

