from django.db import models

from .models import TLabel


class HotLabel():
    id = models.IntegerField
    name = models.CharField(max_length=128)
    hot_point = models.IntegerField
