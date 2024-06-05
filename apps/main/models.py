from django.db import models
from apps.core.models.base_model import BaseModel


class Tag(BaseModel): 
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class StaticData(BaseModel):
    total_students = models.PositiveIntegerField()
    total_graduated = models.PositiveIntegerField()
    average_selary = models.PositiveIntegerField()
    employement = models.PositiveIntegerField()
    student_room_area = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
