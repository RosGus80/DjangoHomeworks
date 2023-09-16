from django.urls import path

from catalog.views import ContactsView, IndexView, PostCreateView, FeedView, PostDetailView

app_name = 'catalog'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('create/', PostCreateView.as_view(), name="create"),
    path('feed/', FeedView.as_view(), name='feed'),
    path('feed/<slug>/', PostDetailView.as_view(), name='post view'),
]
