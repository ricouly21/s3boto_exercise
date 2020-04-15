from django.contrib import admin

from storage.models import Store, StoreFile


class StoreFileAdmin(admin.ModelAdmin):
    exclude = ("file_obj",)


admin.site.register(Store)
admin.site.register(StoreFile, StoreFileAdmin)
