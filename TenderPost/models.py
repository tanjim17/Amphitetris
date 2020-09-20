from django.db import models
from User.models import Profile
from owner.models import Tender


class TenderBid(models.Model):
    vendor = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tender = models.ForeignKey(Tender, on_delete=models.CASCADE)
    price = models.FloatField()
    amount = models.IntegerField()
    product_description = models.CharField(max_length=650)
    delivery_date = models.DateField()

    def __str__(self):
        return str(self.id)