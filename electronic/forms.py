from .models import Electronic, Category
from django.forms import ModelForm, TextInput, Textarea, FileInput, NumberInput

class ElectronicForm(ModelForm):
    class Meta:
        model = Electronic
        fields = ['name', 'brand', 'img', 'price', 'description', 'cat']

        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Наименование'
            }),
            "brand": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Бренд'
            }),
            "img": FileInput(attrs={
                "class": 'form-control',

            }),
            "price": NumberInput(attrs={
                "class": 'form-control',

            }),
            "description": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Описание'
            })

        }