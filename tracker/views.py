from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Company, Device, Employee, DeviceAssign
from .serializers import (
   UserSerializer, CompanySerializer, DeviceSerializer, EmployeeSerializer, DeviceAssignSerializer
)

from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated



class UserAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# Company Views

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    

# Employee Views

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

    


class EmployeeAssignListView(generics.ListAPIView):
    serializer_class = DeviceAssignSerializer
    

    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return DeviceAssign.objects.filter(employee=employee_id)


# Device Views

class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    

    

class DeviceAssignView(generics.UpdateAPIView):
    queryset = DeviceAssign.objects.all()
    serializer_class = DeviceAssignSerializer