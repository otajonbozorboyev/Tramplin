from rest_framework import serializers
from .models import Tag, StaticData


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag')
