from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    choices = [("$", "dollar"), ("₽", "ruble"), ("€", "euro")]
    pos_reklama = models.CharField(choices=choices, max_length=1)
    descr = models.CharField(max_length=256)
