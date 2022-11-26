from rest_framework.permissions import BasePermission
from rest_framework import generics
from backend.accounts.actions.api.user.serializers import UserSerializer
from ..app.models import User


class CreateUserApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes: list[BasePermission] = []