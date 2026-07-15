from import_export import resources
from .models import Account,Employee,Guest


class AccountResource(resources.ModelResource):
     class Meta:
          model = Account
          

class EmployeeResource(resources.ModelResource):
     class Meta:
          model = Employee


class GuestResource(resources.ModelResource):
     class Meta:
          model = Guest