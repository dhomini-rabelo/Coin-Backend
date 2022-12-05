from rest_framework import serializers
from backend.bills.app.models import Bill



class BillSerializer(serializers.ModelSerializer):

    def validate_day(self, value: str | int):
        if str(value).isnumeric() and (int(value) not in range(1, 28)):
            raise serializers.ValidationError('Valor inválido')
        return value

    def validate(self, validated_data: dict):
        if validated_data.get('bill_type') in ['scheduled_income', 'scheduled_expense']:
            if not validated_data.get('day'):
                raise serializers.ValidationError({'day': ['Este campo é obrigatório']})
            elif not validated_data.get('partials'):
                raise serializers.ValidationError({'partials': ['Este campo é obrigatório']})
        else:
            if validated_data.get('day') is not None:
                raise serializers.ValidationError({'day': ['Este campo é inválido']})
            elif validated_data.get('partials') is not None:
                raise serializers.ValidationError({'partials': ['Este campo é inválido']})
        return validated_data

    class Meta:
        model = Bill
        fields = [
            'id', 'user', 'title', 'description', 'bill_type', 'value', 'day', 'partials', 'created_at', 'payment_method'
        ]