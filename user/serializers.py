from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'address']


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, max_length=150)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(required=True, max_length=15)
    address = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone_number', 'address']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number'),
            address=validated_data.get('address')
        )
        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address']