from django.contrib import admin

from catalog.models import Product, Category, Post, Version


# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('price', )
    search_fields = ('name', 'desc')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('name', 'desc', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_published", "views", "date")
    search_fields = ("title", "text")
    list_filter = ("is_published",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'is_active')
    search_fields = ('name', )
    list_filter = ('is_active', )