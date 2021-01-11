from django.db import models
from products.models import Products
from user.models import User
# Create your models here.

class Carts(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, unique=True)
    product_id= models.ManyToManyField(Products, null=True )
    order_time= models.TimeField(auto_now_add=True)   
