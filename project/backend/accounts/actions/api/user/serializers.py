from rest_framework import serializers
from Fast.forms.validators import validate_unique
from backend.accounts.actions.api.user.typings import CreateUserRequestBodyType, CreateUserValidatedDataType
from backend.accounts.app.models import User


class UserSerializer(serializers.ModelSerializer):

    def to_representation(self, instance: User):
        return {
            "email": instance.email,
        }
    
    def validate_email(self, value: str | None):
        if not value:
            raise serializers.ValidationError('Este campo é obrigatório')
        elif not validate_unique(User, 'username', value):
            raise serializers.ValidationError('Este email já foi cadastrado')
        return value

    def validate(self, validated_data: CreateUserValidatedDataType):
        initial_data: CreateUserRequestBodyType = self.initial_data
        if not initial_data.get('confirm_password'):
            raise serializers.ValidationError({'confirm_password': ['Este campo é obrigatório']})
        elif initial_data['confirm_password'] != validated_data['password']:
            raise serializers.ValidationError({'confirm_password': ['As senhas são diferentes']})
        return validated_data        

    def create(self, validated_data: CreateUserValidatedDataType):
        new_user = User(username=validated_data['email'], email=validated_data['email'])
        new_user.set_password(validated_data['password'])
        new_user.save()
        return new_user

    class Meta:
        model = User
        fields = 'email', 'password',


class ChangeEmailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'email',