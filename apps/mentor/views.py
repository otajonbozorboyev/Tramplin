from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.mentor.models import Mentor
from apps.mentor.serializers import MentorSerializer


class MentorAPIVIew(APIView):
    serializer_class = MentorSerializer

    def get(self, request):
        model = Mentor.objects.select_related('mentor_assistant').prefetch_related('tags')
        serializer = self.serializer_class(model, many=True).data
        return Response(serializer)
