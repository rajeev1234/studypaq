import csv
import random

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import filters, status, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response

# Create your views here.
from .models import Locations
from .serializers import LocationSerializer


def home(request):
    locations = Locations.objects.all()
    return render(request,'location/template/home.html',{"locations":locations})

def location_update(request):
    try:
        with open('/home/rajeev/studypad/location/template/location.csv') as f:
                reader = csv.reader(f)
                for row in reader:
                    _, created = Locations.objects.get_or_create(
                        location_id=row[0],
                        location_name=row[1],
                        )
        return JsonResponse({"status":"success"})
    except Exception as ex:
        return JsonResponse({"status":str(ex)})
    

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Locations.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["location_name"]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['location_id'] = random.randint(2000, 10000)
        request.data._mutable = False
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)