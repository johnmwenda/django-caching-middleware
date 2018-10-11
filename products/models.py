from django.db import models

class Product(models.Model):
    # name
    name = models.CharField(max_length=255, null=False)
    # description
    description = models.CharField(max_length=255, null=False)
    # price
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return "{} - {}".format(self.name, self.description)

