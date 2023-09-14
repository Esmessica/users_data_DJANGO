from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #   aditional informations
    personal_web = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', blank=True)


    # user_name = models.CharField(max_length=124)
    # email = models.EmailField(max_length=254, unique=True)
    # age = models.CharField(max_length=3)
    # user_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user.username