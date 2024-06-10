from django.db import models
from apps.core.models.base_model import BaseModel


class Feedback(BaseModel):
    class FEEDBACK_STATUS(models.IntegerChoices):
        NEW = 1, "new"
        CHECKED = 2, "checked"

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=FEEDBACK_STATUS.choices, default=FEEDBACK_STATUS.NEW)

    def __str__(self) -> str:
        return f"{self.full_name}"
