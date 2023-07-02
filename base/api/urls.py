from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView, RegisterAPIView, LoginAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
  path('', views.getRoute),
  path('login/', LoginAPIView.as_view(), name='login'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
  path('register/', RegisterAPIView.as_view(), name='auth_register'),
]
  # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
