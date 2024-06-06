from django.urls import path
from .views import CourseAPIView, CourseModuleAPIView

urlpatterns = [
    path("", CourseAPIView.as_view()),
    path("module/", CourseModuleAPIView.as_view()),
]
