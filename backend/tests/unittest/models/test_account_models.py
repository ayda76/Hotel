import pytest
from rest_framework.test import APIRequestFactory

from account.api.helper import get_tokens_for_user
from tests.factories.account_factory import (AccountFactory,
                                             EmployeeFactory,
                                             GuestFactory)

@pytest.mark.django_db
class TestAccountModel:
    def test_account_create(self):
        account=AccountFactory()
        assert account.id is not None
        
    def test_get_user_jwt_token(self):
        account=AccountFactory()
        token=get_tokens_for_user(account.user)['access']
        print(f"token::{token}")
        factory=APIRequestFactory()
        request=factory.get("/fake-url/", HTTP_AUTHORIZATION=f"Bearer {token}")
        
        result=account.get_user_jwt(request)
        
        assert result == account
        
    def test_account_str(self):
        account=AccountFactory()
        result=f"{account.firstname or ''} {account.lastname or ''}".strip()
        
        assert str(account) == result
@pytest.mark.django_db
class TestEmployee:
    def test_employee_create(self):
        employee=EmployeeFactory()
        assert employee.id is not None
        
    def test_employee_str(self):
        employee=EmployeeFactory()
        result=employee.employee_code
        assert str(employee) == result
        
@pytest.mark.django_db       
class TestGuest:
    def test_guest_create(self):
        guest=GuestFactory()
        assert guest.id is not None
    
    def test_guest_str(self):
        guest=GuestFactory()
        result=guest.account_related.lastname 
        assert str(guest) == result