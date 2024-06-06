from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.feedback_status import FEEDBACK_STATUS


class Feedback(BaseModel):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    status = models.CharField(max_length=255, choices=FEEDBACK_STATUS)

    def __str__(self) -> str:
        return self.full_name
