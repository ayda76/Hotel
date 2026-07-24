from rest_framework import serializers

from reservation.models import Reservation
from account.api.serializers import GuestSerializer
from room.api.serializers import RoomSerializer

class ReservationSimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = '__all__'
        
    def validate(self, attrs):

        room = attrs["room_related"]
        checkin = attrs["checkin_date"]
        checkout = attrs["checkout_date"]

        if Reservation.objects.filter(
            room_related=room,
            checkin_date__lt=checkout,
            checkout_date__gt=checkin,
        ).exists():

            raise serializers.ValidationError(
                "Room is already reserved."
            )

        return attrs
               
class ReservationSerializer(serializers.ModelSerializer):
    guest_related=GuestSerializer(required=False)
    room_related=RoomSerializer(required=False)
    class Meta:
        model = Reservation
        fields = '__all__'
        
        
class ResultReservationSerializer(serializers.Serializer):
    decision = serializers.CharField( choices=[
        ("approve", "approve"), 
        ("reject", "reject")
        ])