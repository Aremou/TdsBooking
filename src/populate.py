#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TdsBooking.settings')

import django
django.setup()

from faker import Faker
from hotels.models import Category, Chambre, Hotel, Equipment, CategoryEquipment
import random


fake = Faker(locale="fr-FR")

hotels = ['Novotel Orisha', 'Link Hôtel', 'Golden Tulip', 'Azalai Hôtel', 'Hôtel du Port', 'Sun Beach Hôtel', 'Hôtel du Lac', 'Nobila Airport Hôtel',
          'Tahiti Hôtel', 'Hotel Mainson Rouge', 'Hotel de la Dispora', 'Villa San Miguel', 'Lagoon Residence', 'La Brume Joyeuse', 'Hôtel Acropole', 'Home Residence Hôtel', 'Ibis Hôtel', 'Paradisia Hôtel', 'Hôtel DK', 'Bénin Royal Hôtel', 'Hotel Pramondo', 'Nora Hôtel', 'Nifur Hôtel', 'i5Hôtel', 'La Lune', 'TDS Hôtel', 'Hôtel des Princes', 'Hôtel Etoile Rouge']
etoiles = ['2', '3', '4', '5', '6', '7', '8']


villes = ['Cotonou', 'Lokossa', 'Ouidah', 'Parakou',
          'Djougou', 'Abomey-Calavi', 'Bohicon', 'Abomey', 'Grand-Popo', 'Dassa', 'Porto-Novo', 'Comey', 'Dogbo', ]


def add_hotel(N):
    for i in range(N):
        h = Hotel.objects.get_or_create(
                name=hotels[i], 
                description=fake.paragraph(), 
                tel_1=fake.phone_number(), 
                token=fake.unique.swift(length=8), 
                email=fake.email(), 
                adress=fake.address(), 
                star_nbr=random.choice(etoiles), 
                ville=random.choice(villes)
            )[0]
        for j in range(10):
            eqt = fake.random_int(min=1, max=700)
            h.equipments.add(eqt)


categories = ['Suite', 'Standard', 'VIP']


def add_cartegorie(N):
    for i in range(N):
        c = Category.objects.get_or_create(
            name=categories[i], description=fake.paragraph())[0]


def add_cartegorie_equipement(N):
    for i in range(N):
        c = CategoryEquipment.objects.get_or_create(
            name=fake.company(), token=fake.unique.swift(length=8))


def add_equipement(N):
    for i in range(N):
        CategoryEquipment = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        e = Equipment.objects.get_or_create(
                name=fake.company(), 
                icon="fa fa-check", 
                category_id=CategoryEquipment, 
                is_admin=1,
                token=fake.unique.swift(length=8)
            )


def add_chambre(N):

    for i in range(N):        
        hotel = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                              '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26'])
        categorie = random.choice(['1', '2', '3'])

        chambre = Chambre.objects.get_or_create(
            name=fake.company(), 
            description=fake.paragraph(), 
            number=fake.unique.random_int(min=1, max=700), 
            overnight=fake.random_int(min=15000, max=900000), 
            token=fake.unique.swift(length=8), 
            area=fake.random_int(min=45, max=100), 
            capacity=fake.random_int(min=1, max=2), 
            category_id=categorie, 
            hotel_id=hotel, 
            beds=fake.random_int(min=1, max=3)
        )[0]
        for j in range(15):
            eqt = fake.random_int(min=1, max=700)
            chambre.equipments.add(eqt)

if __name__ == '__main__':
    print("Populating Script!")

    # add_cartegorie_equipement(10)
    
    add_equipement(700)
    
    # add_hotel(26)

    # add_cartegorie(3)

    # add_chambre(250)


    print("Populating Complete!")
