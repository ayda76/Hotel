from rest_framework.routers import DefaultRouter
from django.urls import path , include ,re_path
from room.api.views import (RoomTypeViewSet,
                             RoomViewSet)


router = DefaultRouter()
router.register("RoomType", RoomTypeViewSet)
router.register("Room",RoomViewSet)


urlpatterns = [

    path("", include(router.urls)),


]
