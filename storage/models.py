from django.db import models
from django.db.models import SET_NULL, CASCADE


def store_file_dir(store_instance, filename):
    instance = store_instance
    return "media/store-{0}/{1}".format(instance.store.id, filename)


class Store(models.Model):
    user = models.ForeignKey("auth.User", null=True, blank=True, on_delete=SET_NULL)
    name = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return "({0}) {1}".format(self.pk, self.name)

    def to_json(self):
        return {"user_id": self.user.id, "name": self.name, "created_at": self.created_at}


class StoreFile(models.Model):
    store = models.ForeignKey("Store", null=True, blank=True, on_delete=CASCADE)
    file_obj = models.FileField(upload_to=store_file_dir, null=True, blank=True)
    filename = models.CharField(max_length=500, null=True, blank=True)
    file_size = models.IntegerField(null=True, blank=True, default=0)
    storage_url = models.CharField(max_length=1000, null=True, blank=True)
    content_type = models.CharField(max_length=100, null=True, blank=True)
    upload_dt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-pk"]

    def __str__(self):
        return "({0}) {1}".format(self.pk, self.filename)

    def to_json(self):
        return {
            "store_id": self.store.pk,
            "filename": self.filename,
            "file_size": self.file_size,
            "storage_url": self.storage_url,
            "content_type": self.content_type,
            "upload_dt": self.upload_dt,
        }
