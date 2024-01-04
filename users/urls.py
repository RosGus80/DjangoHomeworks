from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, verification, UserDetailView, change_password, CheckEmail

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<int:user_pk>/<verification_code>/', verification, name='verification'),
    path('checkemail', CheckEmail.as_view(), name='checkemail'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user'),
    path('user/change_password/<int:pk>', change_password, name='change_password'),
]

