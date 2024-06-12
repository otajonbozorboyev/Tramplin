from rest_framework import serializers

from apps.news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("id", "title", "description", "thumbnail")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'thumbnail' in representation:
            representation['thumbnail'] = 'media/' + representation['thumbnail'].split('/media/')[-1]
        return representation
