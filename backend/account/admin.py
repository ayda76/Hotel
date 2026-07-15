from django.contrib import admin
from import_export.admin import ImportExportModelAdmin 

from .resources import ( AccountResource,
                        EmployeeResource,
                        GuestResource)
from .models import (Account,
                     Employee,
                     Guest)

# Register your models here.


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):

    list_display = ('id','firstname','lastname', )
    resource_class = AccountResource
    
    
@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):

    list_display = ('id','job_title' )
    resource_class = EmployeeResource
    
@admin.register(Guest)
class GuestAdmin(ImportExportModelAdmin):

    list_display = ('id','phone' )
    resource_class = GuestResource