from rest_framework import serializers
from base.models import Products
from django.contrib.auth.models import User


# class UserRegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#     def create(self, clean_data):
#         user_obj = User.objects.create_user(email=clean_data['email'], password=clean_data['password'])
#         user_obj.username = clean_data['username']
#         user_obj.save()
#         return user_obj


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'price', 'available_stock')