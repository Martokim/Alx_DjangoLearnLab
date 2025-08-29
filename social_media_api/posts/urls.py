from django.urls import path
from .views import (
    PostListCreateView,
    PostDetailView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    # --- Posts ---
    path("", PostListCreateView.as_view(), name="post-list-create"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),

    # --- Comments ---
    path("<int:post_id>/comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
]
