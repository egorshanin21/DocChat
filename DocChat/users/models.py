from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.signals import user_logged_in
from django.utils import timezone


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    Attributes:
    - email (EmailField): Field to store the unique email address of the user.

    Methods:
    - __str__(): Method to represent the user object as a string. Returns the username.
    """
    email = models.EmailField(unique=True)
    
    def __str__(self):
        """
        Method to represent the user object as a string.

        Returns:
        - str: Username.
        """
        return self.username