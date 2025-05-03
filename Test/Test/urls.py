
from django.contrib import admin
from django.urls import path, include  # include lets you connect app urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('example.urls')),
]
