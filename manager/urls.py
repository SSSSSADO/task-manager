from django.urls import path

from manager import views


app_name = "manager"

urlpatterns = [
    # Task
    path("", views.TaskListView.as_view(), name="task-list"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    path(
        "<int:pk>/update/",
        views.TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "<int:pk>/delete/",
        views.TaskDeleteView.as_view(),
        name="task-delete"
    ),
    # Tag
    path("tags", views.TagListView.as_view(), name="tag-list"),
]
