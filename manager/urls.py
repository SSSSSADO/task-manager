from django.urls import path

from manager import views


app_name = "manager"

urlpatterns = [
    # Task
    path("", views.TaskListView.as_view(), name="task-list"),
    # Tag
    path("tags", views.TagListView.as_view(), name="tag-list"),
]
