from rest_framework import permissions

class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a task to edit or delete it.
    """

    def has_permission(self, request, view):
        # Allow any authenticated user to access the view
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the task.
        return obj.owner == request.user
