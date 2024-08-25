from django.db import models
from user.models import User

class Farm(models.Model):
    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    size = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Crop(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Animal(models.Model):
    name = models.CharField(max_length=255, unique=True)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
