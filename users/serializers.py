from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from users.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers


class PasswordFieldSerializer(serializers.CharField):
    def __init__(self, **kwargs):
        """
        Adds field that hides password
        :param kwargs:
        """
        kwargs['style'] = {'input_type': 'password'}
        kwargs.setdefault('write_only', True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordFieldSerializer()
    password_repeat = PasswordFieldSerializer()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'lasr_name', 'email', 'password', 'password_repeat')

        """Checking that passwords are correct"""
    def validate(self, attrs: dict) -> dict:
        if attrs['password'] == attrs['password_repeat']:
            return attrs
        raise ValidationError('Passwords must match')

    def create(self, validated_data):
        del validated_data['password_repeat']
        validated_data['password'] = make_password(validated_data['password'])
        return User.objects.create(**validated_data)


class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = PasswordFieldSerializer()

    def create(self, validated_data: dict) -> User:
        if not (user := authenticate(
            username=validated_data['username'],
            password=validated_data['password']
        )):
            raise AuthenticationFailed
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        read_only_fields = ('id', 'username', 'first_name', 'last_name', 'email')
