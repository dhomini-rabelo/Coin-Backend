from rest_framework.permissions import BasePermission
from rest_framework import generics
from Core.api.utils.user import UseAuthenticatedUser
from Core.api.utils.without import WithoutPatch
from backend.accounts.actions.api.user.serializers import ChangeEmailSerializer, ChangePasswordSerializer, UserSerializer
from ..app.models import User


class CreateUserAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes: list[BasePermission] = []


class ChangeEmailAPI(UseAuthenticatedUser, WithoutPatch, generics.UpdateAPIView):
    serializer_class = ChangeEmailSerializer
    queryset = User.objects.all()


class ChangePasswordAPI(UseAuthenticatedUser, WithoutPatch, generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()
