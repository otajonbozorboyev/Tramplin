from rest_framework import serializers
from .models import Tag, StaticData


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
