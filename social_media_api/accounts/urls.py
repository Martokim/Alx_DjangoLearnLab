from django.urls import path
from .views import RegisterView, LoginView, ProfileView, feed_view
from .views import follow_user, unfollow_user
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('feed/', feed_view, name='feed'),
    path('follow/<int:user_id>/', follow_user, name='follow'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow'),
]