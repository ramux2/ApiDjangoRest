from dataclasses import field
from rest_framework import serializers
from frexco import models

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fruit
        fields = '__all__'
