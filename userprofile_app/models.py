from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
    def create_user(self, phone, password=None):
        if not phone:
            raise ValueError('The given Phone must be set')
        phone = self.normalize_email(phone)
        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        user = self.create_user(phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Userprofile(AbstractBaseUser, PermissionsMixin):
    username = None
    phone = models.CharField(max_length=20, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone