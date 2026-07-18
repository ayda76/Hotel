import pytest
from rest_framework.test import APIClient

from account.models import Account,Employee

from tests.factories.account_factory import AccountFactory,EmployeeFactory

@pytest.mark.django_db
def test_employee_list():
    client=APIClient()
    EmployeeFactory.create_batch(5)
    
    response=client.get('/account/Employee/')
    
    assert response.status_code == 200
    
    assert Employee.objects.count() == 5
    
@pytest.mark.django_db
def test_employee_retrieve():
    client=APIClient()
    
    employee=EmployeeFactory()
    
    response=client.get(f"/account/Employee/{employee.id}/")
    
    assert response.status_code == 200
   
    
@pytest.mark.django_db
def test_employee_post():
    client=APIClient()
    account=AccountFactory()

    data={
        "account_related":account.id,
        "employee_code":"test",
        "job_title":"test",
        "address":"xxxxxxx",
        "phone":"0912578976",
        "national_id":"12234567"
    }
    response=client.post(f"/account/Employee/",data)
    
    assert response.status_code == 201
    assert response.data['account_related'] == account.id
    employee = Employee.objects.first()
    employee.refresh_from_db()
    assert employee.account_related.id==account.id
    


@pytest.mark.django_db
def test_employee_patch():
    client=APIClient()

    employee=EmployeeFactory(job_title="title")

    response=client.patch(f"/account/Employee/{employee.id}/",{"job_title":"newjob_title"})
    
    assert response.status_code == 200
    assert response.data['job_title'] == "newjob_title"
    employee = Employee.objects.first()
    employee.refresh_from_db()
    assert employee.job_title=="newjob_title"


@pytest.mark.django_db
def test_employee_delete():

    client=APIClient()

    employee=EmployeeFactory()

    response=client.delete(f"/account/Employee/{employee.id}/")
    
    assert response.status_code == 204
    assert Employee.objects.count()==0   