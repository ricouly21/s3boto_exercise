from django.contrib import admin

from accounts.models import Account


@admin.register(Account)
class AccountsAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
