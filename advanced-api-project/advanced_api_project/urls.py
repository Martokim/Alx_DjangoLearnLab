from django.contrib import admin
from django.urls import path , include 

# Project-level URL configuration
# -Includes 'api.urls' to expose API endpoints under the '/api/' prefix.'

urlpatterns = [
    path('admin/', admin.site.urls),# admin interface URL
    # Include API URLs
    path('api/', include('api.urls')),
    # DRF browsable API login/logout
    path('api-auth/', include('rest_framework.urls')), 
]
