from rest_framework.generics import ListAPIView

from apps.mentor.models import Mentor
from apps.mentor.serializers import MentorSerializer


class MentorAPIVIew(ListAPIView):
    queryset = Mentor.objects.select_related('mentor_assistant').prefetch_related('tags')
    serializer_class = MentorSerializer

    # def get_queryset(self):
    #     #  shuyerdagi malumotni filter qilish kerak yani qanday mentor_assistant bo'lmasa o'sha object kerak emas
    #     pass
