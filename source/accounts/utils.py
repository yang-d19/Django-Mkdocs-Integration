from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

domain_name = "https://dagrad.site"

def send_mail(to, template, context):
    html_content = render_to_string(f'accounts/emails/{template}.html', context)
    text_content = render_to_string(f'accounts/emails/{template}.txt', context)

    msg = EmailMultiAlternatives(context['subject'], text_content, settings.DEFAULT_FROM_EMAIL, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


def send_activation_email(request, email, code):

    url = reverse('accounts:activate', kwargs={'code': code})
    absolute_url = f"{domain_name}{url}"

    context = {
        'subject': _('Profile activation'),
        'uri': absolute_url,
    }

    send_mail(email, 'activate_profile', context)


def send_activation_change_email(request, email, code):

    url = reverse('accounts:change_email_activation', kwargs={'code': code})
    absolute_url = f"{domain_name}{url}"

    context = {
        'subject': _('Change email'),
        'uri': absolute_url, 
    }

    send_mail(email, 'change_email', context)


def send_reset_password_email(request, email, token, uid):

    url = reverse('accounts:restore_password_confirm', kwargs={'uidb64': uid, 'token': token})
    absolute_url = f"{domain_name}{url}"

    context = {
        'subject': _('Restore password'),
        'uri': absolute_url,
    }

    send_mail(email, 'restore_password_email', context)


def send_forgotten_username_email(email, username):
    context = {
        'subject': _('Your username'),
        'username': username,
    }

    send_mail(email, 'forgotten_username', context)
