import datetime

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    desc = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    desc = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='previews/', verbose_name='Картинка', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена')
    date = models.DateTimeField(verbose_name='Дата добавления', null=True, blank=True)
    ChangeDate = models.DateTimeField(verbose_name='Дата последнего изменения', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=100, verbose_name="slug")
    text = models.TextField(verbose_name="содержимое")
    pic = models.ImageField(upload_to='previews/', verbose_name='Картинка', null=True, blank=True)
    date = models.DateTimeField(verbose_name="дата создания", auto_now_add=True)
    is_published = models.BooleanField(verbose_name="признак публикации")
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Версия', null=True, blank=True)
    number = models.FloatField(default=1, verbose_name='Номер версии')
    name = models.CharField(max_length=50, verbose_name='Название версии')
    is_active = models.BooleanField(verbose_name='Признак активной версии')
