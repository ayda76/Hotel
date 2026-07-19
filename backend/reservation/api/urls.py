
from rest_framework.routers import DefaultRouter
from django.urls import path , include ,re_path
from reservation.api.views import ReservationViewSet


router = DefaultRouter()
router.register("Reservation", ReservationViewSet)



urlpatterns = [

    path("", include(router.urls)),


]
