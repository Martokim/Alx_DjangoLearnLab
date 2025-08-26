from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
]
