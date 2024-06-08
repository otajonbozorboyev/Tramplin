from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', include("apps.course.urls")),
    path('student_project/', include("apps.projects.urls")),
    path('mentors/', include("apps.mentor.urls")),
    path('news/', include("apps.news.urls")),
    path('student_feedback/', include("apps.students.urls")),
    path('feedback/', include("apps.feedback.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
