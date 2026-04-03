from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        null=True,
        related_name="tasks",
    )

    class Meta:
        ordering = ["-completed", "-datetime"]

    def __str__(self):
        return f"{self.id}: {self.content} completed: {self.completed}"
