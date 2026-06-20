from django.db import models

class Room(models.Model):

    name = models.CharField(max_length=100)

    room_type = models.CharField(max_length=50)

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(upload_to='rooms/')

    total_rooms = models.IntegerField(default=20)   # ✅ ADD THIS

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name