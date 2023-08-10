import json
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from base.models import Products
from base.api.serializers import ProductSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)


@csrf_exempt
def register(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data['username']
            email = data['email']
            password = data['password']
            password1 = data['password1']
            if username and email and password and password1:
                if password == password1:
                    if User.objects.filter(email=email).exists():
                        message = 'Email already exists'
                        return HttpResponse(message, status=400)
                    elif User.objects.filter(username=username).exists():
                        message = 'Username already exists'
                        return HttpResponse(message, status=400)
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password)
                        user.save();
                        message = 'User created successfully'
                        return JsonResponse(message, safe=False)
                else:
                    message = 'Password not the same'
                    return HttpResponse(message, status=400)
            else:
                message = 'Please fill the required fields'
                return HttpResponse(message, status=400)
        else:
            return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=400)


@csrf_exempt
def product(request, name=None):
    if request.method == 'GET':
        if name != 'no-prod':
            products = Products.objects.filter(name__contains=name)
            products_serializer = ProductSerializer(products, many=True)
            return JsonResponse(products_serializer.data, safe=False)
        else:
            return JsonResponse([], safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
