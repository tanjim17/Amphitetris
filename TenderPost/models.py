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
    SUCCESSFUL = 'SC'
    CANCELLED = 'CC'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESSFUL, 'Successful'),
        (CANCELLED, 'Cancelled'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)
    received_date = models.DateField(null=True)

    def __str__(self):
        return self.bid.tender.tender_title
