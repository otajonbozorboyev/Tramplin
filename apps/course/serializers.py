from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    # category = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('name', 'price', 'icon', 'thumbnail', 'is_active', 'introduction_video', 'course_period_in_month', 'total_lessons', 'total_projects_by_students')

    def get_category(self, obj):
        return 'course'