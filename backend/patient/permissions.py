from rest_framework.permissions import BasePermission


class AllowPostOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST" or request.user and request.user.is_authenticated():
            return True
        return False
