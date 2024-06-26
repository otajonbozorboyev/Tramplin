from django.db import models
from apps.core.models.base_model import BaseModel


class StudentProject(BaseModel):
    title = models.CharField(max_length=255)
    # team_name = models.CharField(max_length=999) # qo'shilishi kere bo'ladigan ish
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    is_selected = models.BooleanField(default=False, null=True, blank=True)
    image = models.FileField(upload_to='media/student_project_images/')
    people_image = models.FileField(upload_to="media/student_project_images/")

    def __str__(self) -> str:
        return f"{self.title}"
