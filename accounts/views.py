from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.viewsets import ModelViewSet

from accounts.models import Account
from accounts.serializers import AccountsSerializer, UserSerializer


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.exclude(
        is_superuser=True,
        is_staff=True
    ).order_by()

    @action(methods=['POST'], detail=False)
    def destroy_all(self, request, *args, **kwargs):
        self.get_queryset().delete()
        return Response({
            'status': HTTP_200_OK,
            'message': 'HTTP_200_OK'
        }, status=HTTP_200_OK)


class AccountsViewSet(ModelViewSet):
    serializer_class = AccountsSerializer
    queryset = Account.objects.select_related(
        'user',
    ).all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        serializer = serializer.create(request.data)
        return Response(serializer.data, status=HTTP_201_CREATED)

    def destroy(self, request, pk=None, *args, **kwargs):
        account = Account(pk=pk)
        account.user.delete()
        return Response({
            'status': HTTP_200_OK,
            'message': 'HTTP_200_OK'
        }, status=HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    def destroy_all(self, request, *args, **kwargs):
        user_ids = [account.user.id for account in self.get_queryset()]
        User.objects.filter(id__in=user_ids).delete()
        return Response({
            'status': HTTP_200_OK,
            'message': 'HTTP_200_OK'
        }, status=HTTP_200_OK)
