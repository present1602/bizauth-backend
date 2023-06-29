from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CreateUserSerializer, CreateProfileSerializer

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


            

class RegisterView(APIView):
  def post(self, request):
    user_data = {
      'user_id': request.data.get('user_id'),
      'password': request.data.get('password'),
    }
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
  