from django.urls import path
from .views import MoviesModelViewSet

urlpatterns = [
    path("", MoviesModelViewSet.as_view())
]
