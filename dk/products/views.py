from product.models import Products, ProductImages,ShippingDetails,Sorts,Types
from products.serializers import ProductsSerializer,ProductIma TypesSerializer,SortsSerializer, ShippingDetailsSerializer
from seller.models import Sellers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from dk.permissions import UserOnly,AllowAny
from auth.backends import UserAuthentication
class ProductView(APIView):

    permission_classes = (AllowAny)
    authentication_classes = []

    @staticmethod
    def get(self,req,*args, **kwargs):

        try:
            if req.town!=null:
                town = req.town
            else:
                town = 'Podgorica'    
            if req.sort!=null:
                Sort = Sorts.objects.get(sort=req.sort)
            elif req.type!=null:
                Sort = Sorts.objects.get(Types__type= req.type)
            if 'Sort' in locals()    
                Products = Products.objects.filter(sort = Sort, ShippingDetails__town = req.town).order_by('packet')
            else:
                Products = Products.objects.filter(sort = Sort, ShippingDetails__town = town).order_by('packet')
            Serializer = ProductsSerializer(instance=Products, many= True)
            return Response({'data': Serializer.data, 'message': "Seller list",
                             'success': True},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data': None, 'message': "Failed to products.",
                             'success': False},
                            status=status.HTTP_503_SERVICE_UNAVAILABLE)
