from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)





