from rest_framework import serializers
from .models import Mentor, MentorAssistant


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('full_name', 'avatar', 'position', 'experience', 'tags', 'is_active')
