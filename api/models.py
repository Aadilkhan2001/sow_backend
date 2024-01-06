from django.db import models

class Terms(models.Model):
    term = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.term

class Product(models.Model):
    name = models.CharField(max_length= 200, blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    in_price = models.PositiveIntegerField(blank=False, null=False)
    in_stock = models.PositiveIntegerField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.name