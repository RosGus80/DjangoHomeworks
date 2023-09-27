from django.urls import path

from catalog.views import ProductsFeedView, ContactsView, IndexView, PostCreateView, FeedView, PostDetailView, \
    PostUpdateView, \
    PostDeleteView, ProductCreateView, ProductUpdateView, ProductDetailView, ProductDeleteView, Joke, VersionCreateView, \
    VersionUpdateView, VersionDeleteView, ProductVersionsView

app_name = 'catalog'


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', PostCreateView.as_view(), name="create"),
    path('feed/', FeedView.as_view(), name='feed'),
    path('feed/<slug>/', PostDetailView.as_view(), name='post view'),
    path('feed/edit/<slug>', PostUpdateView.as_view(), name='update post'),
    path('feed/delete/<slug>', PostDeleteView.as_view(), name='delete post'),
    path('feed/products', ProductsFeedView.as_view(), name='products feed'),
    path('feed/products/create', ProductCreateView.as_view(), name='create product'),
    path('feed/products/update/<int:pk>', ProductUpdateView.as_view(), name='update product'),
    path('feed/products/product/<int:pk>', ProductDetailView.as_view(), name='product view'),
    path('feed/products/delete/<int:pk>', ProductDeleteView.as_view(), name='delete product'),
    path('joke/', Joke.as_view(), name='joke'),
    path('feed/products/create_version', VersionCreateView.as_view(), name='create version'),
    path('feed/products/edit_version/<int:pk>', VersionUpdateView.as_view(), name='update version'),
    path('feed/products/delete_version/<int:pk>', VersionDeleteView.as_view(), name='delete version'),
    path('feed/products/product/<int:pk>/versions/', ProductVersionsView.as_view(), name='versions of product'),
]
