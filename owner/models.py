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
