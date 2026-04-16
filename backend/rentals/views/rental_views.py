from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rentals.models.rental import Rental
from rentals.serializers.rental_serializer import RentalSerializer, CreateRentalSerializer

class isOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
class RentalViewSet(ModelViewSet):
    serializer_class = RentalSerializer
    queryset = Rental.objects.all().order_by('id')

    def get_permissions(self):
        if self.action in ['list', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        if self.action in ['retrieve']:
            return [isOwner()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateRentalSerializer
        return RentalSerializer
        

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.is_staff:
            return Rental.objects.all().order_by('id')
        return Rental.objects.filter(user = user).order_by('id')
    
