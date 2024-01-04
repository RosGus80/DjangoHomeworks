from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, DetailView

from config import settings
from users.forms import UserRegisterForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/login_form.html'
    success_url = reverse_lazy('users:checkemail')

    def form_valid(self, form):
        self.object = form.save()
        self.object.verification_code = User.objects.make_random_password(length=10)

        send_mail(
            subject='Verification email',
            message=f'Follow this link to verify your account: http://127.0.0.1:8000/users/verify/{self.object.pk}/{self.object.verification_code}/',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user.html'


def change_password(request, user_pk):
    user = User.objects.ger(pk=user_pk)
    new_password = user.make_random_password(length=12)
    user.set_password(new_password)
    send_mail(
        subject='Your new password',
        message=f'Your new password is {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email])

    return redirect(reverse_lazy('catalog:checkemail'))


class CheckEmail(TemplateView):
    template_name = 'users/verification.html'


def verification(request, verification_code, user_pk):
    user = User.objects.get(pk=user_pk)
    if user.verification_code == verification_code:
        user.is_verified = True
        user.save()
        return redirect(reverse_lazy(
            'users:login')
        )
    else:
        print('that')
        return redirect(reverse_lazy(
                'catalog:denied')
                )

