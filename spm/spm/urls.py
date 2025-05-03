from django.contrib import admin
from django.urls import path, include
from students import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('', views.landing_page, name='landing'),  # 👈 This will show your page at "/"
]