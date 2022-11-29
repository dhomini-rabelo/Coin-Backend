from rest_framework.response import Response
from rest_framework import status


class WithoutPatch:

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
