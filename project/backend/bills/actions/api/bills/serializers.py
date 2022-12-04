from rest_framework import serializers
from backend.bills.app.models import Bill



class BillSerializer(serializers.ModelSerializer):

    def validate_day(self, value: str | int):
        if not (str(value).isnumeric() and (int(value) in range(1, 28))):
            raise serializers.ValidationError('Valor inválido')
        return value

    class Meta:
        model = Bill
        fields = [
            'id', 'user', 'title', 'description', 'bill_type', 'value', 'day', 'partials', 'created_at',
        ]