from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Post, Version


# Create your views here.


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class IndexView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = Product.objects.all()
        return context_data


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "text", "pic", "is_published", )
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/create.html'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class FeedView(TemplateView):
    template_name = 'catalog/feed.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['posts'] = Post.objects.all()
        return context_data


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "text", "pic", "is_published",)
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/create.html'


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/confirm_delete.html'


class ProductsFeedView(TemplateView):
    template_name = 'catalog/products_feed.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = Product.objects.all()
        return context_data


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = Version.objects.all()
        return context_data


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/confirm_delete_product.html'


class Joke(TemplateView):
    template_name = 'catalog/joke.html'


class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/confirm_delete_product.html'


class ProductVersionsView(DetailView):
    template_name = 'catalog/versions_view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['versions'] = Version.objects.all()
        return context_data
# def home(request):
#     items = Product.objects.all()
#     context = {
#         'products': items
#     }
#     return render(request, 'catalog/home.html', context)

