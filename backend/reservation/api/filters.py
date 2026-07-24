import django_filters
from reservation.models import ReservationStatus,Reservation


class ReservationFilter(django_filters.FilterSet):
    class Meta:
        model= Reservation
        fields={
            'checkin_date':['exact'],
            'checkout_date':['exact'],
            'price':['exact','lt','gt','range'],
            'status':['exact']
            }