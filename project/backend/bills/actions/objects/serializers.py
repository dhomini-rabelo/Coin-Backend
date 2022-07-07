from rest_framework import serializers
from backend.bills.app.models import Bill



class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = 'user', 'title', 'description', 'value', 'is_income', 'day', 'use_notification',