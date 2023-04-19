
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# JLC: from   https://testdriven.io/blog/django-custom-user-model/:
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class BalRucheData(models.Model):
  
  last_date = models.DateTimeField('date de création', auto_now_add=True)
  humid = models.IntegerField('humidité (%)')
  temp  = models.IntegerField('température (°C)')
  masse_ruche1 = models.FloatField("Masse ruche-1")
  masse_ruche2 = models.FloatField("Masse ruche-2")
  masse_ruche3 = models.FloatField("Masse ruche-3")
  masse_ruche4 = models.FloatField("Masse ruche-4")
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
  
  def __str__(self):
    mess = f"{self.last_date.strftime('%Y-%m-%d %H:%M:%S')} by {self.user} ({self.humid:2}%, {self.temp:2}°C) " \
    f"- ({self.masse_ruche1:5.1f},{self.masse_ruche2:5.1f},{self.masse_ruche3:5.1f},{self.masse_ruche4:5.1f}) kg"
    return mess
 