from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14, unique=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']
        db_table = 'company'

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['user']
        db_table = 'Employee'

    def __str__(self):
        return f"{self.user.username}"

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    condition = models.CharField(max_length=255, default='Good')
    serial_number = models.CharField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
        ordering = ['serial_number']
        db_table = 'Device'

    def __str__(self):
        return self.name


class DeviceAssign(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_at_checkout = models.CharField(max_length=255, default='Good')
    condition_at_return = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'DeviceAssign'
        verbose_name_plural = 'DeviceAssign'
        ordering = ['-return_date']  # from top to bottom
        db_table = 'DeviceAssign'

    def __str__(self):
        if self.return_date:
            return f"{self.device.name} returned by {self.employee.user.get_username()} at: ({self.return_date.ctime()})"
        return f"{self.device.name} assigned to {self.employee.user.get_username()}, at: ({self.checkout_date.ctime()})"
