from Fast.django.decorators.cache.api import dinamic_cache_for_api
from backend.bills.actions.api.bills.serializers import BillSerializer
from backend.bills.app.models import Bill
from rest_framework import generics
from Core.controllers.cache import bill_cache



class BillListCreateAPI(generics.ListCreateAPIView):
    serializer_class = BillSerializer

    @property
    def cache_id(self):
        return str(self.request.user.id)

    @property
    def queryset(self):
        return Bill.objects.filter(user__id=self.request.user.id)
    
    def get(self, request):
        return dinamic_cache_for_api(bill_cache, self.cache_id)(super().get)(request)

    def post(self, request):
        if hasattr(request, 'data') and isinstance(request.data, dict):
            request.data['user'] = request.user.id
        return super().post(request)