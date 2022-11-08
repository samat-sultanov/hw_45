from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'created_at']
    list_display_links = ['description']
    list_filter = ['status']
    search_fields = ['description', 'status']
    fields = ['title', 'description', 'status', 'execution_date', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)
