from django.db import models
from user.models import User
from django.utils import timezone

class Grocery(models.Model):
    grocery_name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='grocery')
    prize=models.DecimalField(max_digits=10,decimal_places=2)