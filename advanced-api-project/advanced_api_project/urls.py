from django.contrib import admin
from django.urls import path , include 

# Project-level URL configuration
# -Includes 'api.urls' to expose API endpoints under the '/api/' prefix.'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
