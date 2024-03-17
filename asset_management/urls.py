from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from tracker.views import *
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [

    path('user/', UserAPIView.as_view(), name='user'),
    # for admin
    path('admin/', admin.site.urls),

    # jwt-authentication
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Company URLs
    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),

    # Employee URLs
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('employees/<int:pk>/assign/', EmployeeAssignListView.as_view(), name='employee-Assign-list'),

    # Device URLs
    path('devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view(), name='device-retrieve-update-destroy'),
    path('devices/<int:pk>/assign/', DeviceAssignView.as_view(), name='device-assign'),

    # for swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Automated API documentation
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

  

]
