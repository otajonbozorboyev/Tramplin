from django.urls import path

from apps.projects.views import StudentProjectAPIView, StudentProjectDetailAPIView

urlpatterns = [
    path("", StudentProjectAPIView.as_view()),
    path("<int:pk>/", StudentProjectDetailAPIView.as_view())
]
