from rest_framework.generics import ListAPIView

from apps.news.models import News
from apps.news.serializers.news import NewsSerializer


class NewsAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-id')[:3]
    serializer_class = NewsSerializer
