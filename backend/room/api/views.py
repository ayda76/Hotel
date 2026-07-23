from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, date
from rest_framework.decorators import action

from room.api.serializers import (RoomTypeSerializer,
                                  RoomSerializer,
                                  RoomSimpleSerializer,
                                  RoomChartSerializer)

from room.models import Room,RoomType




class RoomTypeViewSet(viewsets.ModelViewSet):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer
    pagination_class=None
    my_tags = ["Room"]
    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.prefetch_related('room_reservation')
    serializer_class = RoomSerializer
    pagination_class=None
    my_tags = ["Room"]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST','PUT','PATCH']:
            return RoomSimpleSerializer
        return RoomSerializer
    
    @action(detail=True, methods=['get'])
    def roomchart(self,request,pk):
        from reservation.models import Reservation
        room_insatnce=self.get_object()
        
        serializer = RoomChartSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        start_point = serializer.validated_data["start_point"]
        end_point = serializer.validated_data["end_point"]
        
        reservations=Reservation.objects.filter(room_related=room_insatnce,
                                                checkin_date__lt=end_point,
                                                checkout_date__gt=start_point)
        dates=[]
        for rs in reservations:
            dates.extend(rs.reservation_dates)
        
        return Response(dates)
        
        