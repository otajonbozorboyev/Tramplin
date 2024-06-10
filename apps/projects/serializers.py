from rest_framework import serializers

from apps.projects.models import StudentProject


class StudentProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProject
        fields = ("id", "title", "description", "is_active", "is_selected", "image", "people_image")
