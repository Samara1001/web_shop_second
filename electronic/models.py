from django.db import models


class Electronic(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя')
    brand = models.CharField(max_length=30, verbose_name='Марка')
    img = models.ImageField(upload_to='electronic', null=True, blank=True)
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Список электроника'


class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Список категории'

