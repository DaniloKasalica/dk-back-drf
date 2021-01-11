from rest_framework.permissions import BasePermission


class SellerOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_seller


class UserOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user :
            return True
        else :
            return False

class AllowAny(BasePermission):
    def has_permission(self, request, view):
            return True
