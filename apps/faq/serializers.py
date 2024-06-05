from rest_framework import serializers
from .models import FAQ


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = FAQ
        fields = ('course', 'question', 'answer')
