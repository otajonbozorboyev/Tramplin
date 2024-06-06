from django.urls import path

from apps.projects.views import StudentProjectAPIView

urlpatterns = [
    path("", StudentProjectAPIView.as_view())
]
