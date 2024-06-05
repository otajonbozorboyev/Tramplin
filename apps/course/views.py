from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Course
from .serializers import CourseSerializer


class MoviesModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
