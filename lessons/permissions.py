from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    message = "Вы не являетесь модератором!"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        for user in view.get_object().user.all():
            if request.user == user:
                return True
        return False


class IsSuperuser(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
