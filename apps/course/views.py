from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

# from rest_framework.viewsets import ModelViewSet
from .models import Course, CourseModule
from .serializers import CourseSerializer, CourseModuleSerializer


class CourseAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseModuleAPIView(APIView):
    serializer_class = CourseModuleSerializer

    def get(self, request):
        model = CourseModule.objects.select_related("course")  # .all() ertaga ko'rsatiladi
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data)

