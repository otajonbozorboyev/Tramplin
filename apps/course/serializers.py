from rest_framework import serializers
from .models import Course, CourseModule


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'price', 'icon', 'thumbnail', 'is_active', 'introduction_video', 'course_period_in_month', 'total_lessons', 'total_projects_by_students')


class CourseModuleSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = CourseModule
        fields = ['title', 'sequence_number', 'description', 'course']

