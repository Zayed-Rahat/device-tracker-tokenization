import factory
from tracker.models import *


class DeviceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Device

    name = 'Test Device'
    description = "Purchased from ABC company"
    condition = 'Good'
    serial_number = '1234'
    company = 2