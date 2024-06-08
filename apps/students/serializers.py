from rest_framework import serializers

from apps.students.models import StudentFeedback


class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = "__all__"
