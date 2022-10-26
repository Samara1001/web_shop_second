from django.db import models

<<<<<<< HEAD

class Electronic(models.Model):
    name = models.CharField(max_length=40, verbose_name='Имя')
    brand = models.CharField(max_length=30, verbose_name='Марка')
    price = models.FloatField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Электроника'
        verbose_name_plural = 'Список электроника'

=======
# Create your models here.
>>>>>>> 80edc369fe4b1de11ab50780fc8b5bd508116da4
