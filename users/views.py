from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from config import settings
from users.forms import UserRegisterForm
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/login_form.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        self.object = form.save()

        send_mail(
            subject='Verification email',
            message='Congrats',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )

        return super().form_valid(form)




