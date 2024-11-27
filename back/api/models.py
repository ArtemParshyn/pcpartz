from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64)
    tittle = models.CharField(max_length=16)
    price = models.IntegerField()
    descr = models.CharField(max_length=256)
    image = models.ImageField(upload_to="images/%y/%m/%d", blank=False)

    def __str__(self):
        return self.name
