from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   
  profile_pic = models.ImageField(upload_to="profile_pictures", blank=True, null=True)

