from django import template
from django.shortcuts import get_object_or_404
from hotels.models import Category, Hotel, Chambre

from accounts.models import HotelRatings, RoomRatings

register = template.Library()


@register.filter
def min_price(token):

    hotel = get_object_or_404(Hotel, token=token)

    room_list = Chambre.objects.filter(hotel=hotel.id)

    rooms = []

    for room in room_list:
        rooms.append(room.overnight)

    if not rooms:
        return ''
    else:
        return min(rooms)


@register.filter
def get_hotel_score(token):

    hotel = get_object_or_404(Hotel, token=token)

    hotel_ratings = HotelRatings.objects.filter(hotel=hotel.id)

    score = 0
    for rating in hotel_ratings:
        score += rating.score

    return score / len(hotel_ratings) if score else ''


@register.filter
def get_room_score(id):

    room = get_object_or_404(Chambre, pk=id)

    room_ratings = RoomRatings.objects.filter(room=room.id)

    score = 0
    for rating in room_ratings:
        score += rating.score

    return score / len(room_ratings) if score else ''


@register.filter
def get_chambre_by_hotel(item, hotel_id):
    category = Category.objects.get(id=item.id)
    chambres = Chambre.objects.filter(
        category_id=category.id, hotel_id=hotel_id)
    return chambres


@register.filter
def get_hotel_experiences(token):

    hotel = get_object_or_404(Hotel, token=token)

    expreriences = HotelRatings.objects.filter(hotel=hotel.id)

    return expreriences.count()


@register.filter
def get_room_experiences(id):

    room = get_object_or_404(Chambre, pk=id)

    expreriences = RoomRatings.objects.filter(room=room.id)

    return expreriences.count()
