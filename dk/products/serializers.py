from rest_framework import serializers
from .models import Products, Types,Sorts,ShippingDetails,ProductImages
from seller.serializers import SellerSerializer 

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellers
        fields = '[type]'
   
   
class SortsSerializer(serializers.ModelSerializer):
    type = TypesSerializer(many = false)
    class Meta:
        model = Sorts
        fields = '[sort,type]'
  
   
class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '[imageurl]'

class ShippingDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingDetails
        fields = '[time,town]'


class ProductsSerializer(serializers.ModelSerializer):
    product_images= serializers.StringRelatedField(many = True, read_only= True)
    shipping_details= ShippingDetailsSerializer(many = True, read_only= True)
    sort = SortsSerializer(many = False)
    class Meta:
        model = Products
        fields = '[id,product_images,shipping_details,seller,sort,price,availebel,qunatity]'





    def create(self, validated_data):
        product_images = validated_data.pop('product_images')
        shipping_details = validated_data.pop('shipping_details')
        product = Products.objects.create(**validated_data)
        for product_image in product_images:
            Productimages.objects.create(product=product, **product_image )
        for shipping_detail in shipping_details:
            ShippingDetails.objects.create(product=product, **shipping_detail)
        return product  
        
   