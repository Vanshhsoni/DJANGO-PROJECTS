# urls.py
from django.urls import path
from .views import LocationAPI  # Import the LocationAPI class

urlpatterns = [
    path('locations/', LocationAPI.as_view(), name='location-api'),
]
