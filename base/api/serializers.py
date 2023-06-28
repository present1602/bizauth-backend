from .models import User
from rest_framework.serializers import ModelSerializer, EmailField
from django.contrib.auth.hashers import make_password

# class CreateUserSerializer(ModelSerializer):
#     class Meta:
#       model = User
#       fields = ['user_id', 'password', 'user_type', 'phone']
      
#     class Meta:
#       model = Profile
#       fields = ['name', 'email']


# class ProfileSerializer(ModelSerializer):
#   class Meta:
#     model = Profile
#     fields = ['name']
    


class CreateUserSerializer(ModelSerializer):
  email = EmailField(required=False)
  
  class Meta:
    model = User
    fields = ['user_id', 'password', 'user_type', 'phone', 'name', 'email']

def create(self, validated_data):
  # 비밀번호 해싱
  password = validated_data.pop('password')
  hashed_password = make_password(password)

  # User 객체 생성
  user = User.objects.create(password=hashed_password, **validated_data)
  return user
      
      
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
      
      