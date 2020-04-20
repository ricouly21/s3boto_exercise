from django.contrib.auth.models import User
from rest_framework import serializers

from accounts.serializers import AccountsSerializer
from storage.models import Store


class StoreSerializer(serializers.ModelSerializer):
    account = AccountsSerializer(required=False)

    class Meta:
        model = Store
        fields = '__all__'

    # def create(self, validated_data):
    #     print(validated_data)
    #     return Store.objects.all().first()

