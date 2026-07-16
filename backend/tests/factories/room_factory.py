import factory
from faker import Faker
from django.core.files.uploadedfile import SimpleUploadedFile

from room.models import Room, RoomType


fake=Faker()


class RoomTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=RoomType
        
    room_type = 'Standard'
    name         = factory.Faker("name")
    bed_count    = factory.Faker("numerify")
    description  = factory.Faker("text")
    area         = factory.Faker("name")
    


class RoomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Room

    roomtype_related=factory.SubFactory(RoomTypeFactory)
    firstname = factory.Faker("name")
    lastname = factory.Faker("name")
    room_status = 'available'
    price= factory.Faker("numerify")
    floor=factory.Faker("numerify")
    room_code=factory.Faker("numerify")
