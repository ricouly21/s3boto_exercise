from django.db import models
from django.db.models import SET_NULL, CASCADE


class Account(models.Model):
    user = models.OneToOneField('auth.User', null=True, blank=True, on_delete=CASCADE)
    created_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return '({0}) {1}'.format(self.id, self.user.username)

    def save(self, *args, **kwargs):
        if self.user:
            self.created_at = self.user.date_joined
        super(Account, self).save(*args, **kwargs)
