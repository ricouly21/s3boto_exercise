from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from accounts.models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'date_joined',
        )

    def create(self, validated_data):
        user_kwargs = {
            'username': validated_data.get('username'),
            'email': validated_data.get('email'),
            'first_name': validated_data.get('first_name'),
            'last_name': validated_data.get('last_name'),
        }

        self.__init__(data={**user_kwargs})
        if self.is_valid():
            instance = User(**user_kwargs)
            instance.save()
            self.instance = instance
            return Response(self.data, status=HTTP_201_CREATED)

        return None


class AccountsSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Account
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.filter(**{"id": validated_data.get("user_id")}).order_by().first()
        if user:
            instance = Account(user=user)
            instance.save()
            self.instance = instance
            return self

        return None
