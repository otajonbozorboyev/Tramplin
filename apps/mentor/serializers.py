from rest_framework import serializers
from .models import Mentor
from ..main.serializers import TagSerializer


class MentorAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ('full_name', 'avatar')


class MentorSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    mentor_assistant = serializers.SerializerMethodField()

    class Meta:
        model = Mentor
        fields = ("full_name", "avatar", "tags", "mentor_assistant")

    def get_mentor_assistant(self, obj):
        if obj.mentor_assistant is not None:
            return MentorAssistantSerializer(obj.mentor_assistant).data
        return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if representation['mentor_assistant'] is None:
            representation = None
        return representation
