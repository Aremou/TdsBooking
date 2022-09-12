from django.shortcuts import render, redirect

from partenariats.forms import RequestForm

# Create your views here.


def partnerships_conditions(request):
    return render(request, 'partenariats/index.html')


def request_partnerships(request):
    form = RequestForm

    if request.method == 'POST':
        form = RequestForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('request-recap')
    return render(request, 'partenariats/request_partnerships.html', {'form': form})


def recap(request):
    return render(request, 'partenariats/recap.html')
