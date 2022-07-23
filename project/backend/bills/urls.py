from django.urls import path
from .views import *

urlpatterns = [
    path('bills', BillListCreateApi.as_view()),
    path('bills/<int:pk>', BillDetailApi.as_view()),
]
