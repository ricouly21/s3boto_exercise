from django.contrib import admin

from storage.models import Store, StoreFile


@admin.register(Store)
class Store(admin.ModelAdmin):
    pass


@admin.register(StoreFile)
class StoreFileAdmin(admin.ModelAdmin):
    class Meta:
        exclude = ("file_obj",)
