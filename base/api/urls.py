from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView, RegisterAPIView, LoginAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
  path('', views.getRoute),
  path('login/', LoginAPIView.as_view(), name='login'),
  # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('register/', RegisterAPIView.as_view(), name='auth_register'),
  
]
