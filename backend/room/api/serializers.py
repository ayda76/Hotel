from rest_framework import serializers

from room.models import (Room,RoomType)

class RoomTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RoomType
        fields = '__all__'
               
class RoomSerializer(serializers.ModelSerializer):
    roomtype_related=RoomTypeSerializer(required=False)
    class Meta:
        model = Room
        fields = '__all__'
        
class RoomSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'