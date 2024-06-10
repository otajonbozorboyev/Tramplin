from django.urls import path

from apps.main.views import StatisticAPIView

urlpatterns = [
    path("", StatisticAPIView.as_view())
]
