from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, TemplateView

from catalog.models import Product


# Create your views here.


def contacts(request):
    return render(request, 'catalog/contacts.html')


class IndexView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = Product.objects.all()
        return context_data

#
# def home(request):
#     items = Product.objects.all()
#     context = {
#         'products': items
#     }
#     return render(request, 'catalog/home.html', context)


def base_item(request):
    item = Product.objects.all()
    context = {
        'product': item[0]
    }
    return render(request, 'catalog/base.html', context)
