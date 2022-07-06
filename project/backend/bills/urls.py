from django.urls import path
from .views import *

urlpatterns = [
    path('bills', BillListCreateApi.as_view()),
]
