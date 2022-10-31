from django.shortcuts import render
from django.views.generic import DetailView

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


class ElectronicDetailView(DetailView):
    model = Electronic
    template_name = 'electronic/details.html'
    context_object_name = 'electronic'