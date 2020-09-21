from django.db import models

# Create your models here.


class Inventory(models.Model):
    vendor_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=100, choices=[('Fiber', 'Fiber'), ('Fabric', 'Fabric'), (
        'Dye', 'Dye'), ('Chemical and auxiliaries', 'Chemical and auxiliaries')])
    price_per_unit = models.FloatField()
    product_description = models.CharField(max_length=650, default="")

    def __str__(self):
        return str(self.vendor_id) + ': ' + self.product_name


class Orders(models.Model):
    buyer_reg_no = models.IntegerField()
    seller_reg_no = models.IntegerField()
    product_name = models.CharField(max_length=100)
    amount = models.FloatField()
    price = models.FloatField()
    # p = pending, a = accepted, d = denied
    accepted = models.CharField(default='p', max_length=2)
