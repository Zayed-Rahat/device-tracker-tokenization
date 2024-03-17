from django.contrib import admin
from .models import Company, Device, Employee, DeviceAssign

admin.site.site_header = "Asset Tracker API"
admin.site.site_title = "Corporate Asset Tracker Django REST API"
admin.site.index_title = "Welcome Admin"


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone_number')
    search_fields = ('name','location')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    search_fields = ('user', 'company')


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'condition', 'company')
    search_fields = ('name', 'serial_number')


@admin.register(DeviceAssign)
class DeviceAssignAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'checkout_date', 'return_date', 'condition_at_return')
    search_fields = ('device', 'employee__name')
