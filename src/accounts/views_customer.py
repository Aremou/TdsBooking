from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from accounts.models import CustomUser, HotelRatings, RoomRatings
from kkiapay import Kkiapay
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

from django.urls import reverse

from hotels.models import Chambre, Hotel, Payement, Reservation


@login_required(login_url='connexion')
def mes_reservations(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user.id)

    return render(request, 'accounts/customer/reservations/index.html', {'reservations': reservations})


@login_required(login_url='connexion')
def detail_reservation(request, token):

    reservation = get_object_or_404(Reservation, token=token)
    room_rating = ""
    hotel_rating = ""

    try:
        hotel_rating = HotelRatings.objects.get(
            user=request.user.id, hotel=reservation.chambre.hotel_id)
    except HotelRatings.DoesNotExist:
        pass

    try:
        room_rating = RoomRatings.objects.get(
            user=request.user.id, room=reservation.chambre.hotel_id)
    except RoomRatings.DoesNotExist:
        pass

    return render(request, 'accounts/customer/reservations/details.html', {'reservation': reservation, 'hotel_rating': hotel_rating, 'room_rating': room_rating})


@login_required(login_url='connexion')
def annul_reservation(request, token):

    reservation = Reservation.objects.get(token=token)
    reservation.status = "AN"
    reservation.save()

    return HttpResponseRedirect(reverse('reservation', args=[token]))


@login_required(login_url='connexion')
def mes_paiements(request):
    user = request.user

    paiements = Payement.objects.filter(reservation__user=user)

    return render(request, 'accounts/customer/paiements/index.html', {'paiements': paiements})


@login_required(login_url='connexion')
def detail_paiement(request, token):
    paiement = get_object_or_404(Payement, token=token)

    k = Kkiapay('286874f0fedb11eca56ad905c440058f',
                'tpk_28689c01fedb11eca56ad905c440058f', 'tsk_28689c02fedb11eca56ad905c440058f', sandbox=True)
    transaction = k.verify_transaction(paiement.transaction_id)
    return render(request, 'accounts/customer/paiements/details.html', {'paiement': paiement, 'transaction': transaction, })


@login_required(login_url='connexion')
def customer_dashboard(request):

    booking = Reservation.objects.filter(user=request.user.id)
    total = booking.count()
    booking_cancel = booking.filter(status="AN")
    cancel = booking_cancel.count()
    booking_progress = booking.filter(status="EC")
    progress = booking_progress.count()
    booking_end = booking.filter(status="T")
    end = booking_end.count()

    payment = Payement.objects.filter(reservation__user=request.user.id)
    total_payment = payment.count()

    return render(request, 'accounts/customer/dashboard/index.html', {'total': total, 'total_payment': total_payment})


def hotel_ratings(request, token):

    reservation = get_object_or_404(Reservation, token=token)

    if request.method == 'POST':

        customer = CustomUser.objects.get(id=request.user.id)
        customer_hotel = Hotel.objects.get(id=reservation.chambre.hotel_id)

        HotelRatings.objects.update_or_create(
            user=customer,
            hotel=customer_hotel,
            defaults={
                'score': request.POST.get('score'),
                'comments': request.POST.get('comments'),
            })

    return HttpResponseRedirect(reverse('reservation', args=[token]))


def room_ratings(request, token):

    reservation = get_object_or_404(Reservation, token=token)

    if request.method == 'POST':

        customer = CustomUser.objects.get(id=request.user.id)
        customer_room = Chambre.objects.get(id=reservation.chambre.id)

        RoomRatings.objects.update_or_create(
            user=customer,
            room=customer_room,
            defaults={
                'score': request.POST.get('score'),
                'comments': request.POST.get('comments'),
            })

    return HttpResponseRedirect(reverse('reservation', args=[token]))
