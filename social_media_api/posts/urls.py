from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import FollowUserView, UnfollowUserView  

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path("", include(router.urls)),

    #  follow/unfollow routes
    path("users/<int:user_id>/follow/", FollowUserView.as_view(), name="follow-user"),
    path("users/<int:user_id>/unfollow/", UnfollowUserView.as_view(), name="unfollow-user"),
]
