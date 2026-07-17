import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_api_success():
    client=APIClient()
    user=User.objects.create_user(username="test",password="1234")
    
    response=client.post('/account/Login/',{"username":"test","password":"1234"})
    
    assert response.status_code == 200
    
    assert "access" in response.data
    
    
@pytest.mark.django_db
def test_login_api_user_not_exist():
    client=APIClient()
    
    
    response=client.post('/account/Login/',{"username":"test","password":"1234"})
    
    assert response.status_code == 401
    assert "access" not in response.data
    
@pytest.mark.django_db
def test_login_api_worng_input():
    client=APIClient()
    user=User.objects.create_user(username="user1",password="12345")
    
    response=client.post('/account/Login/',{"username":"test","password":"1234"})
    
    assert response.status_code == 401
    assert "access" not in response.data    


@pytest.mark.django_db
def test_login_api_missing_input():
    client=APIClient()
    user=User.objects.create_user(username="user1",password="12345")
    
    response=client.post('/account/Login/',{"username":"",
                                            "password":"12345"})
    
    assert response.status_code == 400
    assert "access" not in response.data    