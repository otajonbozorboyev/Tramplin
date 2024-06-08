from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.students.models import StudentFeedback
from apps.students.serializers import StudentFeedbackSerializer


class StudentFeedbackAPIView(ListAPIView):
    serializer_class = StudentFeedbackSerializer

    def get_queryset(self):
        return StudentFeedback.objects.all().order_by('-id')[:5]


class StudentFeedbackDetailAPIView(RetrieveAPIView):
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentFeedbackSerializer
