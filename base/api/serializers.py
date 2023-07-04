from base.models import User, Profile
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,RefreshToken


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#   @classmethod
#   def get_token(cls, user):
#     token = super().get_token(user)

#     token['user_id'] = user.user_id
#     token['user_uuid'] = str(user.id)

#     refresh = RefreshToken.for_user(user)
#     token['refresh'] = str(refresh)
        
#     return token


# class MyTokenObtainPairView(TokenObtainPairView):
#   serializer_class = MyTokenObtainPairSerializer
      
      
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'


class CreateProfileSerializer(serializers.ModelSerializer):
  user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all()) 
  email = serializers.EmailField(required=False)
  
  class Meta:
    model = Profile
    fields = ['name', 'phone','email', 'user']
    
    
class CreateUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['user_id', 'password']

  def create(self, validated_data):
    password = validated_data.pop('password')
    hashed_password = make_password(password)

    user_instance = User.objects.create(password=hashed_password, **validated_data)
    
    return user_instance
      
# class CreateProfileSerializer(serializers.ModelSerializer):
#   email = EmailField(required=False)
#   user = UserSerializer()
  
#   class Meta:
#     model = Profile
#     fields = ['name', 'phone', 'email', 'user']

#   def create(self, validated_data):
#     user = self.context['request'].user  # 사용자 정보 가져오기
#     validated_data['user'] = user  # 사용자를 profile의 user 필드에 할당

#     return super().create(validated_data)
          

  
    
      
  # def create(self, validated_data):
  #   user = User.objects.create(
  #     validated_data.get('user_id'),
  #     validated_data.get('password'),
  #     validated_data.get('name'),
  #     validated_data.get('phone')
  #   )
  #   return user
   
  # def create(self, validated_data):
  #   profile_data = validated_data.get('profile')
  #   if profile_data:
  #     validated_data.pop('profile')
  #     user = User.objects.create(**validated_data)
  #     # Profile.objects.create(user=user, **profile_data)
      
  #   else:
  #     user = User.objects.create(**validated_data)
  #   return user
      
      
    # profile_data = validated_data.pop('profile')
    # user = User.objects.create(**validated_data)
    # Profile.objects.create(user=user, **profile_data)
    # return user
      
      