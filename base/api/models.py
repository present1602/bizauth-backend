from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


    # profile = Profile.objects.create(user=user, name=name, phone=phone, email=email)
    # profile.save()

class UserManager(BaseUserManager):
  def create_user(self, user_id, password, name, phone, email=None, **extra_fields):
    user = self.model(user_id=user_id, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
        
    
    return user


class User(AbstractBaseUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  user_id = models.CharField(max_length=20, unique=True)
  phone = models.CharField(max_length=11)
  user_type = models.CharField(default='10', max_length=50) #'EMPLOYEE'
  is_active = models.BooleanField(default=True)
  name = models.CharField(max_length=500)
  email    = models.EmailField(unique=True, null=True)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
    
  objects = UserManager()

  USERNAME_FIELD = 'user_id'
    
  class Meta():
    db_table = 'user'


# class Profile(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
#   name = models.CharField(max_length=500)
#   email    = models.EmailField(unique=True, null=True)
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)

#   class Meta():
#     db_table = 'profile'
    
#   def __str__(self):
#       return self.user.name