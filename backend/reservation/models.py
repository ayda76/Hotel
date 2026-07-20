from django.db import models
from datetime import datetime, timedelta, date
from account.models import Guest
from room.models import Room
# Create your models here.
class ReservationStatus(models.TextChoices):
    SUBMITTED = "submitted", "Submitted"
    APPROVED = "approved", "Approved"
    CANCELED = "canceled", "Canceled"
    
class Shift(models.TextChoices):
    DAY = "day", "Day"
    NIGHT = "night", "Night"
    FULLDAY = "fullday", "Fullday"

class Reservation(models.Model):
    
    guest_related    = models.ForeignKey(Guest,related_name="guest_reservation",on_delete=models.CASCADE)
    room_related     = models.ForeignKey(Room,related_name='room_reservation',on_delete=models.CASCADE)   
    #true=day checkin && false=night checkin
    checkin_shift    = models.CharField(max_length=20,choices=Shift.choices,default=Shift.DAY)
    checkin_date     = models.DateField(blank=True,null=True)

    checkout_shift   = models.CharField(max_length=20,choices=Shift.choices,default=Shift.DAY)
    checkout_date    = models.DateField(blank=True,null=True)
    
    price            = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status           = models.CharField(max_length=20,choices=ReservationStatus.choices,default=ReservationStatus.SUBMITTED)
    
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    

    @property
    def days_reservation(self):
        return (self.checkout_date - self.checkin_date).days

    @property
    def reservation_dates(self):
        
        
        if self.checkin_date== self.checkout_date:
            return [{
                "date":self.checkin_date,
                "shift":Shift.FULLDAY
            }]
        
        dates=[]
        day_num = self.days_reservation 
        
        if self.checkin_shift==Shift.DAY: 
            dates.append({
                "date":self.checkin_date,
                "shift":Shift.FULLDAY
            })
        else:
            dates.append({
                "date":self.checkin_date,
                "shift":Shift.NIGHT
            })
            
        for n in range(1, day_num + 1):
            dates.append({
                "date":self.checkin_date+timedelta(days=n),
                "shift":Shift.FULLDAY
            })
        if self.checkout_shift==Shift.DAY:
            dates[-1]['shift']=Shift.DAY
            
        return dates
    
    
    
    def __str__(self):
        return f"{self.guest_related.account_related.lastname} reserved room: {self.room_related.room_code}"
