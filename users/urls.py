from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, VerificationView, EmailVerificationView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login_form.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verification/', VerificationView.as_view(), name='verification'),
    path('email_verification/<uid64>/<token>/', EmailVerificationView.as_view(), name='email')
]

