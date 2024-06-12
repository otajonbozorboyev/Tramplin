from django.db import models
from apps.core.models.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"


class StaticData(BaseModel):
    total_students = models.PositiveIntegerField()
    total_graduated = models.PositiveIntegerField()
    average_selary = models.PositiveIntegerField()
    employment = models.PositiveIntegerField()
    student_room_area = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"


class Statistic(BaseModel):
    mentors = models.SmallIntegerField()
    graduate = models.SmallIntegerField()
    average_salary = models.PositiveIntegerField()
    find_job = models.SmallIntegerField()
    desc = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.mentors}"
