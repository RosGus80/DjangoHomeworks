from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from users.forms import UserRegisterForm
from users.models import User
from users.utils import verification_email


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/login_form.html'
    success_url = reverse_lazy('users:login')


class VerificationView(TemplateView):
    template_name = 'users/verification.html'

    def get(self, request, *args, **kwargs):
        verification_email(request=request, user=request.user)


class EmailVerificationView(View):
    pass



