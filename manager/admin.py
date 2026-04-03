from django.contrib import admin

from manager.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "content", "completed", "datetime", "deadline")
    list_filter = ("completed", "datetime")
    search_fields = ("content",)
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
