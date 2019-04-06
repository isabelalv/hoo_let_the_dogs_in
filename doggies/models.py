from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    kid_friendly = models.IntegerField(default=0)
    dog_friendly = models.IntegerField(default=0)
    low_shedding = models.IntegerField(default=0)
    easy_to_groom = models.IntegerField(default=0)
    high_energy = models.IntegerField(default=0)
    good_health = models.IntegerField(default=0)
    low_barking = models.IntegerField(default=0)
    intelligence = models.IntegerField(default=0)
    easy_to_train = models.IntegerField(default=0)
    tolerates_hot = models.IntegerField(default=0)
    tolerates_cold = models.IntegerField(default=0)
