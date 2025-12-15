from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_admin_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_admin_user = True
        super().save(*args, **kwargs)
