from rest_framework import generics, viewsets


from room.api.serializers import (ReservationSerializer,
                                  ReservationSimpleSerializer)

from reservation.models import Reservation


    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    pagination_class=None
    my_tags = ["Reservation"]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST'or'PUT'or'PATCH':
            return ReservationSimpleSerializer
        return ReservationSerializer