from django.db import models

# Create your models here.


class Demandes(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField()
    TYPE = [
        ('H', 'Hôtel'),
        ('R', 'Restaurant'),
        ('LV', 'Location de voiture'),
    ]
    etablishment_type = models.CharField(choices=TYPE, max_length=200)
    STATUS = [
        ('EC', 'En cours'),
        ('R', 'Rejetée'),
        ('AC', 'Accepteé'),
    ]
    status = models.CharField(choices=STATUS, max_length=200, default='EC')
    date_added = models.DateTimeField(auto_now=True, blank=True, null=True)
