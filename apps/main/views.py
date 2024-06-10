from rest_framework.generics import RetrieveAPIView

from apps.main.models import Statistic
from apps.main.serializers import StatisticSerializer


class StatisticAPIView(RetrieveAPIView):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer

    def get_object(self):
        return Statistic.objects.first()
