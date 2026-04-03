from django.urls import path

from manager import views


app_name = "manager"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task_list"),
]
