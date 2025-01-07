from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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

    title = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_complete(self):
        self.status = 'Completed'
        self.completed_at = timezone.now()
        self.save()

    def mark_incomplete(self):
        self.status = 'Pending'
        self.completed_at = None
        self.save()

    def __str__(self):
        return self.title
