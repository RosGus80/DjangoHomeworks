from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='previews/', verbose_name='Картинка', null=True, blank=True)
    # category =
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateTimeField(verbose_name='Дата добавления')
    ChangeDate = models.DateTimeField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'