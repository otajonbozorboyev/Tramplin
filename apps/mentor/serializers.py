# from rest_framework import serializers
# from .models import Mentor, Assistant
# from ..main.serializers import TagSerializer
#
#
# class MentorAssistantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Assistant
#         fields = ('full_name', 'avatar')
#
#
# class MentorSerializer(serializers.ModelSerializer):
#     mentor_assistant = MentorAssistantSerializer(read_only=True)
#     tags = TagSerializer(many=True)
#
#     class Meta:
#         model = Mentor
#         fields = ("full_name", "avatar", "tags", "mentor_assistant", 'desc')
from rest_framework import serializers

from .models import Assistant, Mentor
from ..main.serializers import TagSerializer


class MentorAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = ('full_name', 'avatar')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'avatar' in representation:
            representation['avatar'] = representation['avatar'].split('/media/')[-1]
        return representation


class MentorSerializer(serializers.ModelSerializer):
    mentor_assistant = MentorAssistantSerializer(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Mentor
        fields = ("id", "full_name", "avatar", "tags", "mentor_assistant", 'desc')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'avatar' in representation:
            representation['avatar'] = 'media/' + representation['avatar'].split('/media/')[-1]
        if 'mentor_assistant' in representation:
            mentor_assistant = representation['mentor_assistant']
            if 'avatar' in mentor_assistant:
                mentor_assistant['avatar'] = 'media/' + mentor_assistant['avatar'].split('/media/')[-1]
        return representation
