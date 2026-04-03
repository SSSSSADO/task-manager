from django import forms

from manager.models import Tag, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
