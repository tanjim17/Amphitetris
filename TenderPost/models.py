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


class PurchaseOrder(models.Model):
    bid = models.ForeignKey(TenderBid, on_delete=models.CASCADE)
    PENDING = 'PD'
    SUCCESS = 'SC'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESS, 'Successful'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.bid.tender.tender_title
