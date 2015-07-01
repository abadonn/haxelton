from django.db import models
from django.contrib.auth.models import User


class UserPreference(models.Model):
    topic = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    user = models.ForeignKey(User)
