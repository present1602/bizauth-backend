from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, CreateProfileSerializer
from django.contrib.auth import authenticate
from datetime import datetime, timedelta

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer
  
      
@api_view(['GET'])
def getRoute(request):
  router = [
    '/api/token',  
    '/api/token/refresh'
  ]
  
  return Response(router)


access_token_expire = timedelta(minutes=2)

class LoginAPIView(APIView):
  def post(selt, request):
    user = authenticate(
      user_id=request.data.get('user_id'),
      password=request.data.get('password')
    )
    
    if user is not None:
      refresh = RefreshToken.for_user(user)
      
      refresh_token = str(refresh)
      access_token = str(refresh.access_token)
      
      resData = {
          'message': 'login success',
          'token': {
              'access': access_token,
              'refresh': refresh_token,
              'access_token_expired_at': (datetime.now() + access_token_expire).strftime(
                "%Y-%m-%d %H:%M:%S")
          },
      }
      
      response = Response(data=resData, status=status.HTTP_200_OK)
      """
        # response.set_cookie(key='access_token', value=access_token, httponly=False, path='/', samesite=None, secure=True)
        # response.set_cookie(key='refresh_token', value=refresh_token, httponly=False, path='/', samesite=None, secure=True)
        # Secure 속성은 HTTPS 연결에서만 쿠키를 전송
        https://stackoverflow.com/questions/46288437/set-cookies-for-cross-origin-requests/46412839#46412839
        when port different set_cookie : Secure=True, samesiteNone & in chrome and firefox
      """
      return response
      
      
    else:
      return Response(status=status.HTTP_400_BAD_REQUEST)
      
      # response = Response(data=resData, status=status.HTTP_200_OK)
      # response.set_cookie(key='access_token', value=access_token, httponly=True)
      # response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)
      # return response
  
            

class RegisterAPIView(APIView):
  def post(self, request):
    user_data = {
      'user_id': request.data.get('user_id'),
      'password': request.data.get('password'),
    }
    print(user_data['user_id'])
    profile_data = {
      'name': request.data.get('name'),
      'phone': request.data.get('phone'),
    }
    email = request.data.get('email')
    if email is not None and email != '':
      profile_data['email'] = email
      
    user_serializer = CreateUserSerializer(data=user_data)

    if user_serializer.is_valid():
      
      user_instance = user_serializer.save()
      profile_data['user'] = user_instance.id
      
      profile_serializer = CreateProfileSerializer(data=profile_data)
      
      if profile_serializer.is_valid():
        profile_serializer.save()
        return Response(status=status.HTTP_200_OK)

      return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
  