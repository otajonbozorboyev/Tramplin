from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.news.models import News
from apps.news.serializers.news import NewsSerializer


class NewsAPIView(APIView):
    serializer_class = NewsSerializer

    def get(self, request):
        model = News.objects.all()
        serializer = self.serializer_class(model, many=True)
        return Response(serializer.data)
