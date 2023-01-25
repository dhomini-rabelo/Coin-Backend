from backend.accounts.actions.api.user.typings import (
    ChangeEmailValidatedDataType, ChangePasswordRequestBodyType,
    ChangePasswordValidatedDataType, CreateUserRequestBodyType,
    CreateUserValidatedDataType
)
from backend.accounts.app.models import User
from Fast.forms.validators import validate_unique
from rest_framework import serializers


class ValidateEmailSupport:

    def validate_email(self, value: str | None):
        if not value:
            raise serializers.ValidationError('Este campo é obrigatório')
        elif not validate_unique(User, 'username', value):
            raise serializers.ValidationError('Este email já foi cadastrado')
        return value



class UserSerializer(ValidateEmailSupport, serializers.ModelSerializer):

    def to_representation(self, instance: User):
        return {
            "email": instance.email,
        }
    
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

    def update(self, instance: User, validated_data: ChangeEmailValidatedDataType):
        if not validated_data.get('email'):
            raise serializers.ValidationError({'email': ['Este campo é obrigatório']})
        return super().update(instance, {**validated_data, 'username': validated_data['email']})

    class Meta:
        model = User
        fields = 'email', 


class ChangePasswordSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {}

    def validate(self, validated_data: ChangePasswordValidatedDataType):
        initial_data: ChangePasswordRequestBodyType = self.initial_data
        user: User = self.instance
        if user.check_password(initial_data.get('current_password')):
            return validated_data
        else:
            raise serializers.ValidationError({'current_password': ['Senha incorreta']})

    def update(self, instance: User, validated_data: ChangePasswordValidatedDataType):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = 'password',


class ChangeNotificationTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'notification_time',



class UserMyAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = 'notification_time',
