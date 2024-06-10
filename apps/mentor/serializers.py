from rest_framework import serializers
from .models import Mentor, Assistant
from ..main.serializers import TagSerializer


class MentorAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ('full_name', 'avatar')


class MentorSerializer(serializers.ModelSerializer):
    mentor_assistant = MentorAssistantSerializer(read_only=True)
    tags = TagSerializer(many=True)
    class Meta:
        model = Mentor
        fields = ("full_name", "avatar", "tags", "mentor_assistant", 'desc')
