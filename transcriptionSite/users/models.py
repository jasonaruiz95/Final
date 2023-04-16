from django.db import models

# Create your models here.


class User(models.Model):

    def __str__(self):
        return (self.username)

    username = models.CharField(max_length=200)
