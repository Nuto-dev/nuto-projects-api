from rest_framework import permissions


class UserViewSetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        else:
            return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user == obj