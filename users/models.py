from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='mail')
    country = models.CharField(max_length=50, verbose_name='country')

    verified = False

    phone = models.CharField(max_length=35, verbose_name='phone')
    avatar = models.ImageField(upload_to='users/', verbose_name='photo', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

