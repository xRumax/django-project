from rest_framework.viewsets import ModelViewSet
from fleet.models.car import Car
from fleet.serializers.car_serializer import CarSerializer

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


    