from django.urls import path

from catalog.views import contacts, home, base_item

app_name = 'catalog'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', base_item, name='product')
]