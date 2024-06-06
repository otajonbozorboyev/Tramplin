from rest_framework.generics import ListAPIView

from apps.projects.models import StudentProject
from apps.projects.serializers import StudentProjectSerializer


class StudentProjectAPIView(ListAPIView):
    serializer_class = StudentProjectSerializer

    #  Bu usul standart sorovlar toplamini sozlash uchun bekor qilingan. get_queryset()
    def get_queryset(self):
        return StudentProject.objects.all().order_by('-id')[:3]
