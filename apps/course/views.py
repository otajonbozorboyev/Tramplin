from rest_framework.generics import ListAPIView
# from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer


class MoviesModelViewSet(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
