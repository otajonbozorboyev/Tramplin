from rest_framework.generics import ListAPIView

from apps.news.models import News
from apps.news.serializers.news import NewsSerializer


class NewsAPIView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self, request):
        return News.objects.all().order_by('-id')[:3]
