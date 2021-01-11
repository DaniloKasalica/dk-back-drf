from django.db import models
from user.models import User
from products.models import Products
class Orders(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    product_id= models.ManyToManyField(Products)
    order_time= models.TimeField(auto_now_add=True)   
