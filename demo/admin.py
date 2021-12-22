from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Employee

admin.site.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
	list_display = ('employee_name','employee_contact','employee_address')

# Register your models here.
