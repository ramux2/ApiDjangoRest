from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50)

class Fruit(models.Model):
    name = models.CharField(max_length=255)
    id_region = models.ForeignKey(to=Region, on_delete=models.CASCADE)