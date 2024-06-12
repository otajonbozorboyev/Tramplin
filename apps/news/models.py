from django.db import models
from django.db.models import CASCADE
from apps.core.models.base_model import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')

    def __str__(self) -> str:
        return f"{self.title}"


class NewsImages(BaseModel):
    image = models.ImageField(upload_to='images/')
    news = models.ForeignKey(News, CASCADE)

    def __str__(self) -> str:
        return f"{self.id}"