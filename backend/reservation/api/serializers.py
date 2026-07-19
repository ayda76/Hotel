from rest_framework import serializers

from reservation.models import Reservation
from account.api.serializers import GuestSerializer
from room.api.serializers import RoomSerializer

class ReservationSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'
               
class ReservationSerializer(serializers.ModelSerializer):
    guest_related=GuestSerializer(required=False)
    room_related=RoomSerializer(required=False)
    class Meta:
        model = Reservation
        fields = '__all__'
        