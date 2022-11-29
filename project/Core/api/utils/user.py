from rest_framework.permissions import BasePermission, IsAuthenticated

class UseAuthenticatedUser:
    permission_classes: list[BasePermission] = [IsAuthenticated]

    def get_object(self):
        return self.request.user