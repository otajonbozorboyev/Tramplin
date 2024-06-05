from django.db.models import CASCADE
from django.db import models
from apps.core.models.base_model import BaseModel
from apps.course.models import Course


class FAQ(BaseModel):
    course = models.ForeignKey(Course, CASCADE, null=True, blank=True)

    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self) -> str:
        return f"{self.id}"
