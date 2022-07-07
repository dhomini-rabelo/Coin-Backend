from backend.bills.actions.objects.serializers import BillSerializer
from backend.bills.app.models import Bill
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


class BillListCreateApi(generics.ListCreateAPIView):
    serializer_class = BillSerializer
    permission_classes = IsAuthenticated,

    @property
    def queryset(self):
        return Bill.objects.filter(id=self.request.user.id)
    
    def post(self, request):
        if hasattr(request, 'data') and isinstance(request.data, dict):
            request.data['user'] = request.user.id
        return super().post(request)
