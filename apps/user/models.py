from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"