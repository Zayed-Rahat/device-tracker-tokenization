import pytest
from rest_framework.test import APIClient
from tracker.tests.demo_data import *

@pytest.mark.django_db
class TestDeviceAPI:
    def test_create_device(self, client: APIClient):
        device_data = {
            'name': DeviceFactory.name,
            'description': DeviceFactory.description,
            'serial_number': DeviceFactory.serial_number,
            'condition': DeviceFactory.condition,
            'company': DeviceFactory.company
        }

        response = client.post('devices/', data=device_data)


