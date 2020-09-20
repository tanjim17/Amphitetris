from django.db import models
from User.models import Profile


class Tender(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    tender_title = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=10)
    description = models.TextField()
    publish_date = models.DateField()
    closing_date = models.DateField()

    def __str__(self):
        return self.tender_title


class PurchaseOrder(models.Model):
    tender = models.OneToOneField(Tender, on_delete=models.CASCADE)
    PENDING = 'PD'
    SUCCESS = 'SC'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (SUCCESS, 'Successful'),
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PENDING)

    def __str__(self):
        return self.tender.tender_title