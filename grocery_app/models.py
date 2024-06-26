from django.db import models
from user.models import User
from django.utils import timezone

class Grocery(models.Model):
    grocery_name = models.CharField(max_length=50)
    image=models.ImageField(upload_to='grocery')
    prize=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.grocery_name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grocery = models.ForeignKey(Grocery, on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.user.username
