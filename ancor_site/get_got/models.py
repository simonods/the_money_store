from django.contrib.auth.models import AbstractUser
from django.db import models


class Article(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()

    class Meta:
        ordering = ["-pub_date"]

    def __str__(self):
        return f"{self.title[:25]}..."



class User(AbstractUser):
    pass
