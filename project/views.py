from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from project import settings


def index_page(request):
    return render(request, 'index.html')


def send_mail_call(request):

    send_mail(
        f'Новая заявка на звонок.',
        f"""У вас заказали новый звонок.
            Телефон: """ + request.GET.get('call'),
        settings.EMAIL_HOST_USER,
        ['info@pcgroup.kz'])

    return redirect('home')