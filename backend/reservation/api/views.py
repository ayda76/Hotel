from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from django.db import transaction
from room.api.serializers import (ReservationSerializer,
                                  ReservationSimpleSerializer)

from reservation.models import Reservation
from account.models import Account,Guest

    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    pagination_class=None
    my_tags = ["Reservation"]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST','PUT','PATCH']:
            return ReservationSimpleSerializer
        return ReservationSerializer
    
    def perform_create(self,serializer):
        with transaction.atomic(): 
            account_login=Account.get_user_jwt(self,self.request)
            guest_related=Guest.objects.get(account_related=account_login)

            serializer.save(guest_related=guest_related)
                
 

        


