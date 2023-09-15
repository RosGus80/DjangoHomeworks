from django.urls import path

from catalog.views import contacts, base_item, IndexView

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', base_item, name='product')
]