from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


    # profile = Profile.objects.create(user=user, name=name, phone=phone, email=email)
    # profile.save()

class UserManager(BaseUserManager):
  def create_user(self, user_id, password, **extra_fields):
    user = self.model(user_id=user_id, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
        
    return user
  
  def create_superuser(self, user_id, password, **extra_fields):
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_staff', True)
    return self.create_user(user_id, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  user_id = models.CharField(validators=[MinLengthValidator(6)], max_length=20, unique=True)
  is_active = models.BooleanField(default=True)
    
  is_staff = models.BooleanField(default=False)  
  objects = UserManager()

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  USERNAME_FIELD = 'user_id'
    
  class Meta():
    db_table = 'user'


class Profile(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  user_type = models.CharField(default='10', max_length=50) #'EMPLOYEE'
  status = models.CharField(default='10', max_length=2) #'EMPLOYEE'
  phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
  name = models.CharField(max_length=500)
  email    = models.EmailField(unique=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  class Meta():
    db_table = 'profile'
    
  def __str__(self):
      return self.user.name