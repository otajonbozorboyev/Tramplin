from django.urls import path

from apps.mentor.views import MentorAPIVIew

urlpatterns = [
    path("", MentorAPIVIew.as_view())
]
