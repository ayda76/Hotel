import pytest
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile

from account.models import Account,Guest
from tests.helper import create_test_image
from tests.factories.account_factory import AccountFactory,GuestFactory

@pytest.mark.django_db
def test_guest_list():
    client=APIClient()
    GuestFactory.create_batch(7)
    
    response=client.get('/account/Guest/')
    
    assert response.status_code == 200
    
    assert Guest.objects.count() ==7
    
@pytest.mark.django_db
def test_guest_retrieve():
    client=APIClient()
    account=AccountFactory()
    guest=GuestFactory(account_related=account)
    
    response=client.get(f"/account/Guest/{guest.id}/")
    
    assert response.status_code == 200
    assert response.data['account_related'] == account.id
    
@pytest.mark.django_db
def test_guest_post():
    client=APIClient()
    account=AccountFactory()

    data={
        "account_related":account.id,
        "passport_img":create_test_image(),
        "nationalcard_img":create_test_image(),
        "phone":"0912578976",
        "address":"xxxxxxxxxxxx"
    }
    response=client.post(f"/account/Guest/",data, format="multipart")
    print(response.data)
    assert response.status_code == 201
    assert response.data['account_related'] == account.id
    guest = Guest.objects.first()
    guest.refresh_from_db()
    assert guest.account_related.id==account.id
    


@pytest.mark.django_db
def test_guest_patch():
    client=APIClient()
    account=AccountFactory()
    guest=GuestFactory(account_related=account)

    response=client.patch(f"/account/Guest/{guest.id}/",{"phone":"9123456737"})
    
    assert response.status_code == 200
    assert response.data['phone'] == "9123456737"
    account = Guest.objects.first()
    guest.refresh_from_db()
    assert str(guest.phone)=="9123456737"


@pytest.mark.django_db
def test_guest_delete():

    client=APIClient()

    guest=GuestFactory()

    response=client.delete(f"/account/Guest/{guest.id}/")
    
    assert response.status_code == 204
    assert Guest.objects.count()==0   