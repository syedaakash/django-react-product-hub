import json
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
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
            if password == password1:
                if User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exists')
                    return HttpResponse(status=400)
                elif User.objects.filter(username=username).exists():
                    messages.info(request,'Username already exists')
                    return HttpResponse(status=400)
                else:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    user.save();
                    return JsonResponse({"message": "success"},safe=False)
            else:
                messages.info(request,' Password not the same')
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)
    except Exception:
        return HttpResponse(status=400)



@csrf_exempt
def product(request):
    if request.method == 'GET':
        # if id:
        #     selected_product = Products.objects.get(pk=id)
        #     if 'selected_products' in request.session:
        #         if id not in request.session['selected_products']:
        #             if is_sel:
        #                 request.session['selected_products'].append(id)
        #         else:
        #             if not is_sel:
        #                 request.session['selected_products'].remove(id)
        #     else:
        #         if is_sel:
        #             request.session['selected_products'] = [id]
        #     product_serializer=ProductSerializer(selected_product)
        #     request.session.modified = True
        #     selected_products = request.session['selected_products'] if 'selected_products' in request.session else []
        #     context = {'product_serializer': product_serializer.data, 'selected_products': selected_products}
        #     return JsonResponse(context,safe=False)
        # else:
        products = Products.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
