from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rentals.models.rental import Rental
from rentals.serializers.rental_serializer import RentalSerializer

class RentalViewSet(ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Rental.objects.filter(user = self.request.user).order_by('id')