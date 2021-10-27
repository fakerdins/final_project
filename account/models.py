import re
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.crypto import get_random_string

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is empty...')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('Email field is empty...')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.create_activation_code()
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=35, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email} | {self.username}'

    def create_activation_code(self):
        code = get_random_string(length=12)
        self.activation_code = code
        self.save()
