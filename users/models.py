from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser
    """
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Optional profile fields
    bio = models.TextField(blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.username
