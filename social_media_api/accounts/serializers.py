from rest_framework import serializers
from django.contrib.auth import get_user_model , authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token 



User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for returning user details"""

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    """Serializer for registering a new user"""
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={"input_type": "password"},
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "password2"]
    #validate if both passwords match
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = get_user_model().objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class UserLoginSerializer(serializers.Serializer):
    """Serializer for logging in a user"""
    username = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, 
        style={"input_type": "password"}
        )

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        attrs["user"] = user
        return user
