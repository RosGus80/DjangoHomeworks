from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


class GetCachedCategories:
    """
    Caches the categories if the cache is enabled, or retrieves them from the database.
    Returns:
        category_list: A list of Category objects.
    """
    @staticmethod
    def cache_categories(*args, **options):

        if settings.CACHE_ENABLED:
            category_list = cache.get('categories')
            if category_list is None:
                category_list = Category.objects.all()
                cache.set('categories', category_list)

    @staticmethod
    def get_cached_list():
        if settings.CACHE_ENABLED:
            return cache.get('categories')
