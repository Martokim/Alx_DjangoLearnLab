from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, profile_view

urlpatterns =[

    path('', auth_view.LoginView.as_view(template_name='blog/login.html'),name='home')
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'),name='logien')
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    
    ]