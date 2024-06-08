from rest_framework import generics

from apps.feedback.models import Feedback
from apps.feedback.serializers import FeedbackSerializer


class StudentFeedbackCreateAPIView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save()
