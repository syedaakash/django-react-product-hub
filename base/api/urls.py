from django.urls import path, re_path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    # path('register/', views.register),
    re_path(r'^register$',views.register),
    re_path(r'^product/$',views.product),
    # path('product/<name>', views.product),
    # re_path(r'^product/(?P<id>\d+)/$',views.product),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]