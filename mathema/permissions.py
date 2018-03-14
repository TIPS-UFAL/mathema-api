from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow teacher of an object to edit it.
    """

    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to a teacher.
        return request.user.user_type == 2


class IsTeacher(permissions.BasePermission):
    """
        Custom permission to only allow teacher of an object to edit and to see it.
    """
    def has_permission(self, request, view):
        return request.user.user_type == 2


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
        Custom permission to only allow the Owner of an object to edit and to see it.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
