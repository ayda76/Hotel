from django.db import models
from datetime import datetime, timedelta, date
from account.models import Guest
from room.models import Room
# Create your models here.



class Reservation(models.Model):
    guest_related    = models.ForeignKey(Guest,related_name="guest_reservation",on_delete=models.CASCADE)
    room_related     = models.ForeignKey(Room,related_name='room_reservation',on_delete=models.CASCADE)   
    date_reserved   = models.DateField()
    #true=day checkin && false=night checkin
    checkin_shift   = models.BooleanField(default=True)
    nights          = models.IntegerField(default=0)
    days            = models.IntegerField(default=0)
    checkout_shift  = models.BooleanField(default=True)

    is_canceled            = models.BooleanField(default=False)
    created_at             = models.DateTimeField(auto_now_add=True)
    updated_at             = models.DateTimeField(auto_now=True)
    
    @property
    def price_reservation(self):
        return self.room_related.price*((self.nights+self.days)/2)
    def __str__(self):
        return f"{self.guest_related.account_related.lastname} reserved room: {self.room_related.room_code}"
