from rest_framework import serializers
from ..models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('full_name', 'phone_number', 'status')
