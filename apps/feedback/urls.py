from django.urls import path

from apps.feedback.views import StudentFeedbackCreateAPIView

urlpatterns = [
    path("", StudentFeedbackCreateAPIView.as_view())
]
