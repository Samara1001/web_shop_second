from django.shortcuts import render
from .models import Electronic


def index(requests):
    return render(requests)


def main(request):
    return render(request)


def electronic(request):
    return render(request)