from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('id', 'title', 'owner', 'priority', 'status', 'due_date', 'completed_at')  
    search_fields = ('title', 'description', 'owner__username')  # Allow searching by task title, description, and owner's username
    list_filter = ('priority', 'status', 'due_date')  # Filters for the sidebar in admin
    fields = ('title', 'description', 'owner', 'priority', 'status', 'due_date', 'completed_at')  # Fields to display on detail view
    readonly_fields = ('completed_at',)  # Make completed_at read-only

    def get_queryset(self, request):
        """
        Limit queryset to tasks owned by the current user in the admin panel.
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all tasks
        return qs.filter(owner=request.user)  # Other users see only their tasks
