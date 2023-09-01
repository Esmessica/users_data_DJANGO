from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User(models.Model):

    user_name = models.CharField(max_length=124)
    email = models.EmailField(max_length=254, unique=True)
    age = models.CharField(max_length=3)
    user_id = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)