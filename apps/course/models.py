from django.db import models
from django.db.models import CASCADE, SET_NULL
from apps.core.models.base_model import BaseModel
from apps.mentor.models import Mentor


class Course(BaseModel):
    mentor = models.ForeignKey(Mentor, SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    icon = models.ImageField(upload_to="Course/Icon", null=True, blank=True)
    thumbnail = models.ImageField(upload_to="Course/Thumbnail", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    introduction_video = models.FileField(null=True, blank=True)
    course_period_in_month = models.PositiveIntegerField()
    total_lessons = models.PositiveIntegerField()
    total_projects_by_students = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class CourseModule(BaseModel):
    course = models.ForeignKey(Course, CASCADE)

    title = models.CharField(max_length=255, null=True, blank=True)
    sequence_number = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class CourseModuleIcons(BaseModel):
    course_module = models.ForeignKey(CourseModule, CASCADE)

    image = models.ImageField(upload_to="Course", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.id}"
