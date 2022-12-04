from django.urls import path
from . import api

urlpatterns = [
    path('bills', api.BillListCreateAPI.as_view()), # route used in backend/bills/app/signals.py
]
