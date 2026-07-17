import pytest
from rest_framework.test import APIClient

from django.contrib.auth.models import User
from account.models import Account
from account.api.helper import get_tokens_for_user
from tests.factories.account_factory import AccountFactory,UserFactory

@pytest.mark.django_db
def test_account_list():
    client=APIClient()
    AccountFactory.create_batch(5)
    
    response=client.get('/account/Account/')
    
    assert response.status_code == 200
    
    assert Account.objects.count() == 5
    
@pytest.mark.django_db
def test_account_retrieve():
    client=APIClient()
    user=UserFactory()
    account=AccountFactory(user=user)
    
    response=client.get(f"/account/Account/{account.id}/")
    
    assert response.status_code == 200
    assert response.data['user'] == user.id
    
@pytest.mark.django_db
def test_account_post():
    client=APIClient()
    user=UserFactory()

    data={
        "user":user.id,
        "firstname":"test",
        "lastname":"test",
        "email":"aa@gmail.com",
        "phone":"0912578976"
    }
    response=client.post(f"/account/Account/",data)
    
    assert response.status_code == 201
    assert response.data['user'] == user.id
    account = Account.objects.first()
    account.refresh_from_db()
    assert account.user.id==user.id
    


@pytest.mark.django_db
def test_account_patch():
    client=APIClient()
    user=UserFactory()
    account=AccountFactory(user=user)

    response=client.patch(f"/account/Account/{account.id}/",{"firstname":"newone"})
    
    assert response.status_code == 200
    assert response.data['firstname'] == "newone"
    account = Account.objects.first()
    account.refresh_from_db()
    assert account.firstname=="newone"


@pytest.mark.django_db
def test_account_delete():

    client=APIClient()

    account=AccountFactory()

    response=client.delete(f"/account/Account/{account.id}/")
    
    assert response.status_code == 204
    assert Account.objects.count()==0   