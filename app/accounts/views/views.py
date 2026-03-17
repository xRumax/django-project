from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from accounts.models.user import User
from accounts.serializers.user_serializer import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]