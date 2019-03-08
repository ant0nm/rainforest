from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
