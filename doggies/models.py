from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
