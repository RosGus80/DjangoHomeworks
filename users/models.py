from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    name = models.CharField(max_length=50, default='', verbose_name='name')
    email = models.EmailField(unique=True, verbose_name='mail')
    country = models.CharField(max_length=50, verbose_name='country')

    is_verified = models.BooleanField(default=False, verbose_name='verified')
    verification_code = models.CharField(max_length=10, default='', verbose_name='verification code', null=True, blank=True)

    phone = models.CharField(max_length=35, verbose_name='phone')
    avatar = models.ImageField(upload_to='users/', verbose_name='photo', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

