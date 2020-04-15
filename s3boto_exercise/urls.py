from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from s3boto_exercise.settings import STATIC_URL, STATIC_ROOT
from storage.views import StoreViewSet, StoreFileViewSet

router = DefaultRouter()
router.register("store", StoreViewSet, basename="stores")
router.register("store/(?P<store_pk>[^/.]+)/files", StoreFileViewSet, basename="store-files")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/admin/", admin.site.urls),
]

urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
