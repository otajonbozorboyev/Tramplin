from django.db import models
from django.db.models import CASCADE
from apps.core.models.base_model import BaseModel


class StudentProject(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_selected = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

class StudentProjectImages(BaseModel):
    image = models.ImageField(upload_to='media/student_project_images/')
    student_project = models.ForeignKey(StudentProject, CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"