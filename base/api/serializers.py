from rest_framework import serializers
from base.models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'available_stock')