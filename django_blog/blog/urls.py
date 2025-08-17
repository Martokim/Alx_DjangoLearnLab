from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, logout_view, profile_view 


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
