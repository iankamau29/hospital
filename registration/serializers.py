from rest_framework import serializers
from .models import product
from .models import shoes


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'


class shoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = shoes
        fields = '__all__'
