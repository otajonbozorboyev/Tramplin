from django.db import models
from apps.core.models.base_model import BaseModel


class Student(BaseModel):
    full_name = models.CharField(max_length=200)
    avatar = models.ImageField(null=True)
    position = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.full_name


class StudentFeedback(BaseModel):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="student_feedback/video")
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
