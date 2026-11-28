from rest_framework import permissions


class WorkRelationPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.member == request.user