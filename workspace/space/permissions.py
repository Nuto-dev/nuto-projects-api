from rest_framework.permissions import BasePermission


class WorkSpacePermission(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner