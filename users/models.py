from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    coin = models.IntegerField(default=0)  # Example additional field

    def __str__(self):
        return self.username
