from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
# tasks/models.py
from django.utils import timezone

class Task(models.Model):
    ...
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_complete(self):
        self.status = 'Completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        self.status = 'Pending'
        self.completed_at = None
        self.save()


# Create your models here.
