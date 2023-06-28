from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
  path('', views.getRoute),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('register/', views.RegisterView.as_view(), name='auth_register'),
  
]
