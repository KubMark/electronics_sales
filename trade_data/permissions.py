from rest_framework.permissions import BasePermission


class IsActivePermission(BasePermission):
    message = 'You have no access'

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
