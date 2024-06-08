from django.urls import path

from apps.students.views import StudentFeedbackAPIView, StudentFeedbackDetailAPIView

urlpatterns = [
    path("", StudentFeedbackAPIView.as_view()),
    path("<int:pk>/", StudentFeedbackDetailAPIView.as_view()),
]
