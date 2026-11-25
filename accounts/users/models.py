from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    username = models.CharField(max_length=52, unique=True)
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username