from rest_framework import generics
from backend.bills.actions.objects.serializers import BillSerializer
from backend.bills.app.models import Bill


class BillListCreateApi(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
