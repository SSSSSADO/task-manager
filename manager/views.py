from django.shortcuts import render
from django.views import generic

from manager.models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
