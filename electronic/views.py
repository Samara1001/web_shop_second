from django.shortcuts import render
from django.views.generic import DetailView, UpdateView


from django.shortcuts import render, redirect
from .models import Electronic, Category
from .forms import ElectronicForm


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

def create(request):
    error = ''
    if request.method == 'POST':
        form = ElectronicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = ElectronicForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'electronic/create_page.html', data)


class ElectronicUpdateView(UpdateView):
    model = Electronic
    template_name = 'electronic/update.html'

    form_class = ElectronicForm


