from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsOwnerOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Task objects. Requires user authentication.
    """
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOnly]
    queryset = Task.objects.all()


    def get_queryset(self):
        """
        Return only the tasks that belong to the authenticated user.
        """
        if self.request.user.is_superuser:
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)  

    def perform_create(self, serializer):
        """
        Automatically assign the currently authenticated user to the task.
        """
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing User objects.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Consider restricting this further

class IsOwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a task to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        """
        Write permissions are only allowed to the owner of the task.
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user  # Corrected field name

class APIRootView(APIView):
    """
    Custom root view for the API.
    """
    def get(self, request, *args, **kwargs):
        return Response({
            "tasks": request.build_absolute_uri("tasks/"),
            "users": request.build_absolute_uri("users/"),
        })
    



class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

