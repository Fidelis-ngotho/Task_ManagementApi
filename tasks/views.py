from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOnly

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Task objects. Requires user authentication.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    

    def perform_create(self, serializer):
        """
        Automatically assign the currently authenticated user to the task.
        """
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Return tasks that belong to the authenticated user
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the task owner when creating a new task
        serializer.save(owner=self.request.user)





class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User objects.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



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
