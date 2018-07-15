from django.db import models
from django.conf import settings

# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, "CASCADE")
    studentname = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.user)