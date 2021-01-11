from django.db import models
from seller.models import Seller
 
class Types(models.Model):
    type = models.CharField(max_length=30, unique=True, blank=False ) 
 
    def __str__(self):
        return self.Type

class Sorts(models.Model):
    type = models.ForeignKey(Types, related_name='sort',on_delete=models.CASCADE)
    sort= models.CharField(max_length=30, unique=True, blank=False )
 
    def __str__(self):
        return self.sort
 
class Products(models.Model):
    seller = models.ForeignKey(Seller, related_name='products',on_delete=models.CASCADE)
    sort = models.ForeignKey(Sorts, related_name='products',on_delete=models.CASCADE)
    product_name= models.CharField(max_length=30, unique=True, blank=False )
    price= models.FloatField(null=True) 
    availebel = models.BooleanField(default=False, blank= False)
    quantity = models.IntegerField(null = True)
    unit = models.CharField(max_length=3, null = True)
    createdtime= models.TimeField(auto_now_add=True)   
 
    def __str__(self):
        return self.product_name
 
class ShippingDetails(models.Model):
    product= models.ForeignKey(Products, related_name='shipping_details',on_delete=models.CASCADE)
    time= models.IntegerField(null=True) 
    town= models.CharField(max_length=30, unique=True, blank=False )
    def __str__(self):
        return self.time

class ProductImages(models.Model):
    imageurl= models.CharField(max_length=30, unique=True, blank=False,null=False )
    product = models.ForeignKey(Products,related_name='productimages',on_delete=models.PROTECT)
 
    def __str__(self):
        return self.imageurl               
 