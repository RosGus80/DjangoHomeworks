from django.shortcuts import render

from catalog.models import Product


# Create your views here.


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    items = Product.objects.all()
    context = {
        'products': items
    }
    return render(request, 'catalog/home.html', context)


def base_item(request):
    item = Product.objects.all()
    context = {
        'product': item[0]
    }
    return render(request, 'catalog/base_item.html', context)
