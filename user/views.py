from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
