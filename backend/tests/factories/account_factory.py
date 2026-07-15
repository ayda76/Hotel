import factory
from faker import Faker
from django.core.files.uploadedfile import SimpleUploadedFile

from account_app.models import Account, Employee,Guest
from django.contrib.auth.models import User

fake=Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=User
        
    username = factory.Sequence(lambda n: f"user{n}")
    is_staff = True
    


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Account

    user=factory.SubFactory(UserFactory)
    firstname = factory.Faker("name")
    lastname = factory.Faker("name")
    email = factory.Sequence(lambda n: f"user{n}@test.com")

    phone=factory.Faker("numerify", text="0912578976")
    img = factory.LazyFunction(
        lambda: SimpleUploadedFile(
            "avatar.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
    )

class EmployeeFactory(factory.django.DjnagoModelFactory):
    class Meta:
        model=Employee   
    account_related=factory.subFactory(AccountFactory)
    employee_code=factory.Faker("name")
    job_title=factory.Faker("name")
    address=factory.Faker("text")
    phone=factory.Faker("numerify", text="0912578976")
    national_id=factory.Faker("numerify", text="1363310783")


class GuestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model=Guest
        
    account_related=factory.subFactory(AccountFactory)
    passport_img = factory.LazyFunction(
        lambda: SimpleUploadedFile(
            "passport_img.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
    )
    nationalcard_img=factory.LazyFunction(
        lambda: SimpleUploadedFile(
            "nationalcard_img.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
    )
    phone=factory.Faker("numerify", text="0912578988")
    address=factory.Faker("text")
