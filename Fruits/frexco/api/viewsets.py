from rest_framework import viewsets
from frexco.api import serializers
from frexco import models

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RegionSerializer
    queryset = models.Region.objects.all()

class FruitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FruitSerializer
    queryset = models.Fruit.objects.all()
