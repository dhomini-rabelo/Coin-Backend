from backend.accounts.actions.api.user.serializers import UserMyAccountSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.response import Response
from rest_framework import status
from backend.accounts import User


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        user = User.objects.get(username=request.data['username'])

        return Response({
            "tokens": serializer.validated_data,
            "user": UserMyAccountSerializer(instance=user).data,
        }, status=status.HTTP_200_OK)
