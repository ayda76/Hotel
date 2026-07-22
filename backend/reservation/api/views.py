from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError

from room.api.serializers import (ReservationSerializer,
                                  ReservationSimpleSerializer)

from reservation.models import Reservation
from account.models import Account,Guest

    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    pagination_class=None
    my_tags = ["Reservation"]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST'or'PUT'or'PATCH']:
            return ReservationSimpleSerializer
        return ReservationSerializer
    
    def perform_create(self,serializer):
        try:
            account_login=Account.get_user_jwt(self,self.request)
            guest_related=Guest.objects.get(account_related=account_login)
            if guest_related is not None:
                instance=serializer.save(guest_related=guest_related)
                return instance
        except:
            raise ValidationError({"detail":"reservation failed"}) 