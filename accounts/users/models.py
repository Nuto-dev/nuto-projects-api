from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email