from django.db import models
from django.db.models import CASCADE
from apps.core.models.base_model import BaseModel
from apps.main.models import Tag


class Mentor(BaseModel):
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField()
    position = models.PositiveIntegerField()
    experience = models.DateField()
    tags = models.ManyToManyField(Tag)
    is_active = models.BooleanField(default=True)
    mentor_assistant = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="assistant"
    )

    def __str__(self) -> str:
        return self.full_name
