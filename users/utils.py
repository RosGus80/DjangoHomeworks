from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def verification_email(request, user):
    site = get_current_site(request)
    context = {
        'domain': site.domain,
        'first_name': user.first_name,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),

    }
    message = render_to_string(
        template_name='users/verification_email.html',
        context=context)
    email = EmailMessage(
        subject='Verification email',
        body=message,
        to=[user.email],
        from_email='noreply@mail.com'
    )
    email.send()

