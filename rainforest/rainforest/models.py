from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError

min_length = MinLengthValidator(limit_value=10)


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=500, validators=[min_length])
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def price_in_dollars(self):
        dollars = self.price / 100
        return "${:.2f}".format(dollars)
