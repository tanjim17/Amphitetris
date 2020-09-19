from django.db import models

# Create your models here.


class Inventory(models.Model):
    vendor_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=10)
    price_per_unit = models.FloatField()

    def __str__(self):
        return str(self.vendor_id)+': ' + self.product_name
