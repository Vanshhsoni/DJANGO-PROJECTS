# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Location
from .serializers import LocationSerializer

class LocationAPI(APIView):
    def post(self, request):
        data = request.data
        location = Location.objects.create(
            device_id=data.get('device_id'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude')
        )
        return Response({"message": "Location saved successfully!"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
