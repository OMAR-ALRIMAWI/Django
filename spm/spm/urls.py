from django.contrib import admin
from django.urls import path, include  # ✅ path is imported here
from students.views import StudentLoginView, landing_page

from django.conf import settings                     # ✅ for serving static
from django.conf.urls.static import static           # ✅ for serving static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', landing_page, name='landing'),
    path('student-login/', StudentLoginView.as_view(), name='student_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])