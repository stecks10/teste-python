from rest_framework import serializers
from frexco_fruits import models

class RegionSerializer(serializers.ModelSerializer):
  class Meta: 
    model = models.Region
    fields = '__all__'
    

class FruitSerializer(serializers.ModelSerializer):
  class Meta: 
    model = models.Fruit
    fields = '__all__'
    depth = 1