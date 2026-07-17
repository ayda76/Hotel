import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from account.models import Account
from account.api.helper import get_tokens_for_user


@pytest.mark.django_db
def test_passwordchange_success():
    user=User.objects.create_user(username='test',password='test')
    account=Account.objects.create(user=user)
    
    client=APIClient()
    token = get_tokens_for_user(user)["access"]

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )
    
    response=client.post('/account/change/password/',{
            "old_password": "test",
            "new_password1": "12345",
            "new_password2": "12345"
    })
    
    assert response.status_code == 200
    
    user.refresh_from_db()
    assert user.check_password(
        "12345"
    )
    

@pytest.mark.django_db
def test_passwordchange_wrong_password():
    user=User.objects.create_user(username='test',password='test')
    account=Account.objects.create(user=user)
    
    client=APIClient()
    token = get_tokens_for_user(user)["access"]

    client.credentials(
        HTTP_AUTHORIZATION=f"Bearer {token}"
    )
    
    response=client.post('/account/change/password/',{
            "old_password": "other_test",
            "new_password1": "12345",
            "new_password2": "12345"
    })
    
    assert response.status_code == 400
    

@pytest.mark.django_db
def test_passwordchange_not_login():
    user=User.objects.create_user(username='test',password='test')
    account=Account.objects.create(user=user)
    
    client=APIClient()

    
    response=client.post('/account/change/password/',{
            "old_password": "test",
            "new_password1": "12345",
            "new_password2": "12345"
    })
    
    assert response.status_code == 401
    
    

    