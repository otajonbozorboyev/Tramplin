from django.urls import path
from .views import CourseAPIView, CourseModuleAPIView, CourseDetailAPIView

urlpatterns = [
    path("", CourseAPIView.as_view()),
    path("<int:pk>/", CourseDetailAPIView.as_view()),
    path("module/", CourseModuleAPIView.as_view()),
]
