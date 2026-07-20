from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action

from room.api.serializers import (RoomTypeSerializer,
                                  RoomSerializer,
                                  RoomSimpleSerializer)

from room.models import Room,RoomType




class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    pagination_class=None
    my_tags = ["Room"]
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    pagination_class=None
    my_tags = ["Room"]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST'or'PUT'or'PATCH':
            return RoomSimpleSerializer
        return RoomSerializer
    
    @action(detail=True, methods=['get'])
    def roomchart(self,request,pk):
        room_insatnce=self.get_object()
        reservations=room_insatnce.room_reservation.all()
        