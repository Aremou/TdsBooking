from django import template
from django.shortcuts import get_object_or_404
from hotels.models import Hotel, Chambre

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
