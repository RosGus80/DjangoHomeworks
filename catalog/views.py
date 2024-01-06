from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import View
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView
from catalog.services import GetCachedCategories

from catalog.forms import ProductForm, VersionForm, ProductModerForm
from catalog.models import Product, Post, Version, Category


# Create your views here.


class AccessDeniedView(TemplateView):
    template_name = 'catalog/access_denied.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


class IndexView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = Product.objects.all()
        return context_data


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ("title", "text", "pic", "is_published", )
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/create.html'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.author = self.request.user
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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ("title", "text", "pic", "is_published",)
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/create.html'

    def test_func(self):
        if self.request.user.has_perm('catalog.change_post') or self.get_object().author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('catalog:feed')
    template_name = 'catalog/confirm_delete.html'

    def test_func(self):
        if self.request.user.has_perm('catalog.delete_post') or self.get_object().author == self.request.user:
            return True
        else:
            return False


class ProductsFeedView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/products_feed.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['products'] = Product.objects.all()
        return context_data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.create_product'
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'

    def form_valid(self, form):
        product = form.save(commit=False)
        product.author = self.request.user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'

    def test_func(self):
        if self.get_object().author == self.request.user:
            return True
        elif self.request.user.groups.filter(name='ProductModer').exists():
            self.form_class = ProductModerForm
            return True
        else:
            return False


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['versions'] = Version.objects.all()
    #     return context_data


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/confirm_delete_product.html'

    def test_func(self):
        if self.request.user.has_perm('catalog.delete_product') or self.get_object().author == self.request.user:
            return True
        else:
            return False


class Joke(TemplateView):
    template_name = 'catalog/joke.html'


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/create.html'


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:products feed')
    template_name = 'catalog/confirm_delete_product.html'


class ProductVersionsView(DetailView):
    template_name = 'catalog/versions_view.html'
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            versions_list = cache.get(f'version_set_{self.object.pk}')
            if versions_list is None:
                versions_list = self.object.version_set.all()
                cache.set(f'version_set_{self.object.pk}', versions_list)
        else:
            versions_list = self.object.version_set.all()

        context_data['versions'] = versions_list

        return context_data


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_all.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        command = GetCachedCategories.get_cached_list()
        context_data['objects'] = command.get_cached_list()

        return context_data


# def home(request):
#     items = Product.objects.all()
#     context = {
#         'products': items
#     }
#     return render(request, 'catalog/home.html', context)

