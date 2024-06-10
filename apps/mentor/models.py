from django.db import models
from apps.core.models.base_model import BaseModel
from apps.main.models import Tag


class Assistant(models.Model):
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="assistant/")
    position = models.PositiveIntegerField()
    experience = models.DateField()
    is_active = models.BooleanField(default=True)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.desc} | {self.full_name}"


class Mentor(BaseModel):
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="mentor/")
    position = models.PositiveIntegerField()
    experience = models.DateField()
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    desc = models.CharField(max_length=500)
    mentor_assistant = models.ForeignKey(Assistant, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.full_name}"
