
from rest_framework import status
from django.contrib.auth import authenticate
from user.models import User,UserToken
from user.serializers import UserLoginSerializer, UserRegistrationSerializer,UserTokenSerializer,UserLogOutSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from dk.permissions import UserOnly,AllowAny
from auth.backends import UserAuthentication
from cart.models import Carts


class UserLogin(APIView):
    authentication_classes=[]
    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserLogout(APIView):
    authentication_classes = [UserAuthentication]
    permission_classes = (AllowAny,)
    serializer_class = UserLogOutSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class RefreshTokenUser(APIView):
    authentication_classes = []
    permission_classes = (AllowAny,)
    def post(self, request):
        try:
            serializer = UserTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data': None, 'message': "Failed to products.",
                             'success': False},
                            status=status.HTTP_400_BAD_REQUEST)    
 
class UserRegistration(APIView):
    permission_classes = (AllowAny,)
    authentication_classes=[]
    serializer_class = UserRegistrationSerializer
 
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        try:
            Carts.objects.create(user_id=user)
        except Exception as e:
            print(e)
            return Response({'data': None, 'message': "Failed to products.",
                             'success': False},
                            status=status.HTTP_400_BAD_REQUEST)         
        return Response(serializer.data, status=status.HTTP_201_CREATED)                                 