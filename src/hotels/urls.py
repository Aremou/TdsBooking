from django.urls import path
from hotels.views import booking_recap, showRoom, hotel_check_avail, hotel_detail, hotels_view, pay_process, reservation_hotel, search_hotel, transition

urlpatterns = [
    path('', hotels_view, name="hotels-index"),
    path('<str:slug>/', hotel_detail, name='hotel'),
    path('<str:slug>/chambre-<int:number>/',
         showRoom, name='chambre'),
    path('<str:slug>/chambre-<int:number>/reservation/',
         reservation_hotel, name='reservation'),
    path('reservation', search_hotel, name='name_search_hotel'),
    path('paiement/<str:token>/<str:type>/paiement-process/',
         pay_process, name='paiement_process'),

    path('<str:slug>/verifier-les-disponibiltes/',
         hotel_check_avail, name='check-hotel-avail'),

    path('reservation-<str:token>/recap/',
         booking_recap, name='recap'),

    path('transition/<str:token>/<str:type>/', transition, name='transition'),


]
