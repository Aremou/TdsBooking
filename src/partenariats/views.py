from django.shortcuts import render

# Create your views here.


def partnerships_conditions(request):
    return render(request, 'partenariats/index.html')


def request_partnerships(request):
    return render(request, 'partenariats/request_partnerships.html')
