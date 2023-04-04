from django.db import models
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    pages = models.CharField(max_length=5)
    publishing_company = models.CharField(max_length=50)
    users = models.ManyToManyField(
        User, through="followings.Following", related_name="books"
    )
