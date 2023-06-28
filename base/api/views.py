from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from .serializers import CreateUserSerializer


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
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      
      return Response(status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


      # user = User.objects.create_user(
      #     user_id=serializer.validated_data['user_id'],
      #     password=serializer.validated_data['password'],
      #     name=serializer.validated_data['name'],
      #     phone=serializer.validated_data['phone'],
      #     email=serializer.validated_data.get('email')
      # )
      # profile = Profile.objects.create(
      #     user=user,
      #     name=serializer.validated_data['name'],