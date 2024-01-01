from django.conf import settings
from django.core.cache import cache
from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        if settings.CACHE_ENABLED:
            category_list = cache.get('categories')
            if category_list is None:
                category_list = Category.objects.all()
                cache.set('categories', category_list)
        else:
            category_list = Category.objects.all()

    @staticmethod
    def get_cached_list():
        if settings.CACHE_ENABLED:
            return cache.get('categories')


