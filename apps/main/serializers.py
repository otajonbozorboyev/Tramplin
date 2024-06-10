from rest_framework import serializers
from .models import Tag, Statistic


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = ("mentors", "graduate", "average_salary", "find_job", "desc")
