from django.contrib import admin
from django.urls import path, include  # Include is required for app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  # Include dashboard app URLs
    path('api/', include('api.urls')),  # Include API app URLs
]
