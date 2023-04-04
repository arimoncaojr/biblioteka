from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=150, unique=True)
    is_employee = models.BooleanField(default=False, null=True, blank=True)
    is_blocked = models.BooleanField(default=False, null=True, blank=True)
    blocked_until = models.DateTimeField(default=None, null=True)
