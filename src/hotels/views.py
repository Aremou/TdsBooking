from ast import arg
from curses.ascii import NUL
import decimal
import string
import random
import dateparser

from django.utils.crypto import get_random_string
from django.core.paginator import Paginator
from datetime import date, datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
import requests
from accounts.models import CustomUser
from hotels.models import Category, Chambre, Equipement, Equipement_Hotel, Hotel, Image_Chambre, Image_Hotel, Payement, Reservation

from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


from hotels.helpers.availability import check_availability


def search_hotel(request):
    if 'date' in request.GET:
        date = request.GET['date']
        t = date.split("-")
        t1 = t[0]
        t2 = t[1]
    elif 'date1' in request.GET:
        t1 = request.GET['date1']
        t2 = request.GET['date2']

    search = request.GET['search']

    price = []

    request.session['date01'] = t1
    request.session['date02'] = t2

    room_list = Chambre.objects.filter(
        hotel__ville=search).exclude(is_delete=True)

    available_hotels = []
    available_hotels_by_price = []
    for room in room_list:
        if check_availability(room, t1, t2):
            available_hotels.append(room.hotel_id)

    set_hotel = set(available_hotels)

    for item in set_hotel:
        chambres = Chambre.objects.filter(
            hotel_id=item).exclude(is_delete=True)
        for chambre in chambres:
            price.append(chambre.overnight)
        available_hotels_by_price.append(
            {'hotel': chambre.hotel, 'price': min(price)})
        price.clear()

    hotels_number = len(set_hotel)
    message = f' {hotels_number} établissements trouvés'

    if hotels_number == 1 or hotels_number == 0:
        message = f'{hotels_number} établissement trouvé'

    return render(request, 'hotels/hotels/search.html', {'available_hotels_by_price': available_hotels_by_price, 'message': message, 'lieu': search, 'd1': t1, 'd2': t2})


def hotels_view(request):

    t1 = ""
    t2 = ""

    if request.session.get('date01', False):
        t1 = request.session['date01']
        t2 = request.session['date02']

    hotels = Hotel.objects.all()
    chambres = Chambre.objects.all().exclude(is_delete=True)
    paginator = Paginator(hotels, 9)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'hotels/hotels/index.html', context={"hotels": page_object, "chambres": chambres, 'd1': t1, 'd2': t2})


def hotel_detail(request, slug):

    hotel = get_object_or_404(Hotel, slug=slug)
    t1 = request.session.get('date01')
    t2 = request.session.get('date02')

    room_list = Chambre.objects.filter(hotel=hotel.id)
    imgs = Image_Hotel.objects.filter(hotel=hotel.id)
    hotel_categories = Category.objects.all()

    available_rooms = []
    if t1 and t2:
        for room in room_list:
            if check_availability(room, t1, t2):
                available_rooms.append(room)

    equipements = Equipement_Hotel.objects.filter(hotel=hotel.id)

    return render(request, 'hotels/hotels/hotel.html', context={"hotel": hotel, "chambres": available_rooms, "equipements": equipements, "imgs": imgs, "hotel_categories": hotel_categories})


def hotel_check_avail(request, slug):
    hotel = get_object_or_404(Hotel, slug=slug)
    date = request.GET['date']
    t = date.split("-")
    t1 = t[0]
    t2 = t[1]
    request.session['date01'] = t1
    request.session['date02'] = t2
    return HttpResponseRedirect(reverse('hotel', args=[hotel.slug]))


def chambre_detail(request, slug, number):

    print('t')
    chambre = get_object_or_404(Chambre, number=number)
    hotel = get_object_or_404(Hotel, slug=slug)
    equipements = Equipement.objects.filter(chambre=chambre.id)
    imgs = Image_Chambre.objects.filter(chambre=chambre.id)

    return render(request, 'detail_chambre.html', context={"chambre": chambre, "hotel": hotel, "equipements": equipements, "imgs": imgs})


def scret_key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def reservation_hotel(request, slug, number):

    resp = requests.get("https://restcountries.com/v3.1/all")

    countries = resp.json

    key = scret_key_generator()
    while Reservation.objects.filter(secret_key=key).exists():
        key = scret_key_generator()

    token = get_random_string(length=32)
    while Reservation.objects.filter(token=token).exists():
        token = get_random_string(length=32)

    chambre = Chambre.objects.get(number=number)
    hotel = Hotel.objects.get(slug=slug)
    a = request.session.get('date01')
    b = request.session.get('date02')
    mode = request.POST.get('check')
    x1 = dateparser.parse(a)
    x2 = dateparser.parse(b)
    sejour = (x2 - x1).days
    amount = chambre.overnight * sejour
    user = ""
    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        tel = request.POST.get('tel')

        password = ''
        characters = list(string.ascii_letters +
                          string.digits + "!@#$_/[]%&()")

        for i in range(8):
            password += random.choice(characters)

        if CustomUser.objects.filter(email=email).exists():
            user = CustomUser.objects.get(email=email)

        else:
            user = CustomUser.objects.create_user(
                first_name=first_name, date_joined=datetime.now(), last_name=last_name, email=email, password=password, tel=tel,)

            template = render_to_string('hotels/email/new_user.html', {
                'first_name': first_name, 'last_name': last_name, 'password': password, 'email': email})
            mail = EmailMessage(
                'TDS Booking',
                template,
                settings.EMAIL_HOST_USER,
                [email],
            )
            mail.fail_silently = False
            mail.send()

        reserv = Reservation.objects.create(
            user_id=user.id, secret_key=key, token=token, chambre_id=chambre.id, check_in=x1, check_out=x2, amount=amount)
        print(reserv.token)
        return HttpResponseRedirect(reverse('transition', args=[reserv.token, request.POST.get('check')]))

    return render(request, 'hotels/reservation/index.html', context={"chambre": chambre, "hotel": hotel, "date1": a, "date2": b, "amount": amount, "sejour": sejour, "countries": countries})


def transition(request, token, type):

    reserv = Reservation.objects.get(token=token)

    return render(request, 'hotels/transition.html', {'type_paiement': type, 'reservation': reserv})


def pay_process(request, token, type):

    transaction_id = request.GET['transaction_id']
    reserv = Reservation.objects.get(token=token)

    token = get_random_string(length=32)
    while Payement.objects.filter(token=token).exists():
        token = get_random_string(length=32)

    Payement.objects.create(transaction_id=transaction_id, token=token, payment_method=type,
                            reservation_id=reserv.id)
    Reservation.objects.filter(token=token).update(status='EC')

    template = render_to_string('hotels/email/confirmation_booking.html', {
        'reserv': reserv})

    mail = EmailMessage(
        'TDS Booking | Confiramtion',
        template,
        settings.EMAIL_HOST_USER,
        [reserv.user.email],
    )

    mail.fail_silently = False

    mail.send()

    return HttpResponseRedirect(reverse('recap', args=[reserv.token]))


def booking_recap(request, token):
    reserv = Reservation.objects.get(token=token)
    x1 = dateparser.parse(str(reserv.check_in))
    x2 = dateparser.parse(str(reserv.check_out))
    sejour = (x2 - x1).days
    return render(request, 'hotels/reservation/recap.html', {"reserv": reserv, "sejour": sejour})
