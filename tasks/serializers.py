from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'owner', 'completed_at']
        read_only_fields = ['completed_at', 'owner']

    def validate(self, data):
        # Check if user is authenticated
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError("You must be logged in to create a task.")
        
        # Validate due date
        if data.get('due_date') <= timezone.now().date():
            raise serializers.ValidationError("Due date must be in the future.")
        
        return data

    def create(self, validated_data):
        # Associate the task with the authenticated user
        validated_data['owner'] = self.context['request'].user  # Corrected field name
        return super().create(validated_data)
