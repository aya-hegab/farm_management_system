from django.shortcuts import render
from rest_framework import viewsets
from .models import Farm, Crop, Animal
from .serializers import FarmSerializer, CropSerializer, AnimalSerializer
from user.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(farm__owner=self.request.user)

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return self.queryset.filter(farm__owner=self.request.user)