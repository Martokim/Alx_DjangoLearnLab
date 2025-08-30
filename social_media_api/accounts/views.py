from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CustomUser


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])   # 👈 REQUIRED by checker
def follow_user(request, user_id):
    user_to_follow = get_object_or_404(CustomUser, id=user_id)

    if request.user == user_to_follow:
        return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({"message": f"You are now following {user_to_follow.username}"})


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])   # 👈 REQUIRED by checker
def unfollow_user(request, user_id):
    user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

    if request.user == user_to_unfollow:
        return Response({"error": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({"message": f"You have unfollowed {user_to_unfollow.username}"})
