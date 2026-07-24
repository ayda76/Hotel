from rest_framework import generics, viewsets,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.decorators import action

from django.db import transaction

from django_filters.rest_framework import DjangoFilterBackend

from room.api.serializers import (ReservationSerializer,
                                  ReservationSimpleSerializer,
                                  ResultReservationSerializer)
from account.models import Account,Guest
from reservation.models import Reservation,ReservationStatus
from reservation.api.filters import ReservationFilter


    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    pagination_class=None
    my_tags = ["Reservation"]
    filterset_class=ReservationFilter
    filterfilter_backends=[DjangoFilterBackend, ]
    
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method in ['POST','PUT','PATCH']:
            return ReservationSimpleSerializer
        return ReservationSerializer
    
    def perform_create(self,serializer):
        with transaction.atomic(): 
            account_login=Account.get_user_jwt(self,self.request)
            guest_related=Guest.objects.get(account_related=account_login)

            serializer.save(guest_related=guest_related)
            
    #add permission permission_classes=[IsHotelEmployee]        
    @action(detail=True, methods=['post'],)
    def review_submitted_reservations(self,request,pk):
        
        reservation = self.get_object()
        
        if reservation.status != ReservationStatus.SUBMITTED:
            raise ValidationError( {"detail": "Reservation has already been processed."} )
        
        with transaction.atomic():
            serializer = ResultReservationSerializer(data=request.data)
        
            serializer.is_valid(raise_exception=True)
            result=serializer.validated_data['decision']
            if result =='approve':
                reservation.status=ReservationStatus.APPROVED
                reservation.save(update_fields=["status"])
                #email sent to guest
            
            elif result =='reject':
                reservation.status=ReservationStatus.REJECTED
                reservation.save(update_fields=["status"])
                #send email to guest
            else:
                raise ValidationError({"detail":"action failed"})
            
            return Response({"detail": "Reservation approved."},status=status.HTTP_200_OK)

        
        
 

        


