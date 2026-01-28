from rest_framework.permissions import BasePermission


class IsAdminOrAnalyst(BasePermission):
    message = "Requires analyst or admin role."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_staff:
            return True
        return request.user.roles.filter(name__in=["analyst", "admin"]).exists()
