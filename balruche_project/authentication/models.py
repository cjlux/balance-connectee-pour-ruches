from django.contrib.auth.models import AbstractUser
from django.db import models

# JLC: from   https://testdriven.io/blog/django-custom-user-model/:
#      puis https://openclassrooms.com/fr/courses/7192426-allez-plus-loin-avec-le-framework-django/7386368-personnalisez-le-modele-utilisateur

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email