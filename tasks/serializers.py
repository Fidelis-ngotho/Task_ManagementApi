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
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError("You must be logged in to create a task.")
        return data

