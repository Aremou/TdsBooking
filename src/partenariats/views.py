from email.message import EmailMessage
from django.shortcuts import render, redirect
from TdsBooking import settings

from partenariats.forms import RequestForm
from django.template.loader import render_to_string


# Create your views here.


def partnerships_conditions(request):
    return render(request, 'partenariats/index.html')


def request_partnerships(request):
    form = RequestForm

    if request.method == 'POST':
        form = RequestForm(request.POST)
        email = request.POST['email']

        if form.is_valid():
            form.save()
            template = render_to_string(
                'partenariats/email/partenariat.html', {})
            mail = EmailMessage(
                'TDS Booking',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            mail.fail_silently = False
            mail.send()
            return redirect('request-recap')
    return render(request, 'partenariats/request_partnerships.html', {'form': form})


def recap(request):
    return render(request, 'partenariats/recap.html')
