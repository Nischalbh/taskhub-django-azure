from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
        "priority",
        "due_date",
        "completed",
        "created_at",
    )
    list_filter = (
        "priority",
        "completed",
    )
    search_fields = ("title", "user__username")
