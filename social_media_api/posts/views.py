from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets, permissions, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics, permissions, status

from notifications.models import Notification


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post/comment.
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    """
    CRUD for Post objects.
    Users can only update/delete their own posts.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['author__username']
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']


class CommentViewSet(viewsets.ModelViewSet):
    """
    CRUD for Comment objects.
    Users can only update/delete their own comments.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter
    ]
    filterset_fields = ['post']
    ordering_fields = ['created_at']
    ordering = ['created_at']

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    """
    Authenticated users can like a post.
    """
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response(
            {'error': 'You have already liked this post.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    # generate notification for the post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
    return Response(
        {'message': 'Post liked successfully.'},
        status=status.HTTP_200_OK
    )

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    """
    Authenticated users can unlike a post.
    """
    post = generics.get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response(
            {'message': 'Post unliked successfully.'},
            status=status.HTTP_200_OK
        )
    except Like.DoesNotExist:
        return Response(
            {'error': 'You have not liked this post.'},
            status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def feed(request):
    """
    Returns posts from users the current user follows,
    ordered by most recent first.
    """
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)
