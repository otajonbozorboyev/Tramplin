from django.urls import path

from apps.news.views import NewsAPIView

urlpatterns = [
    path("", NewsAPIView.as_view())
]
