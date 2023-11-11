from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone


class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.username