from django.db import models
from main.models import Room

class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    number_of_rooms = models.IntegerField()   
    total_price = models.FloatField()         

    def __str__(self):
        return self.name