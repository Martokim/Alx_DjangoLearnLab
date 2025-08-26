from django.urls import path, include

urlpatterns = [
    path("api/accounts/", include("accounts.urls")),
]
