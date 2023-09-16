from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView

from catalog.models import Product, Post


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

# def home(request):
#     items = Product.objects.all()
#     context = {
#         'products': items
#     }
#     return render(request, 'catalog/home.html', context)

