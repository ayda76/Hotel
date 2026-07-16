from django.db import models

# Create your models here.


class RoomType(models.Model):
    SELECT_TYPE  = (('Standard','Standard'),('Deluxe','Deluxe'),('Suite','Suite'),('Presidential','Presidential'))
    room_type    = models.CharField(max_length=20,choices=SELECT_TYPE,default='Standard')
    name         = models.CharField(max_length=200)
    bed_count    = models.IntegerField(default=0)
    description  = models.TextField()
    area         = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    SELECT_STATUS    = (('available','available'),('Occupied','Occupied'),('repairing','repairing'),('Reserved','Reserved'))
    room_code        = models.DecimalField(max_digits=11, decimal_places=0)
    room_status      = models.CharField(max_length=100,choices=SELECT_STATUS,default='available')
    roomtype_related = models.ForeignKey(RoomType,related_name='type_room',on_delete=models.CASCADE)
    price            = models.PositiveIntegerField(default=0)
    floor            = models.PositiveIntegerField(default=0)
    