from django.db import models
#from User.models import Profile
from django.contrib.auth.models import User


class Tender(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tender_title = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=10)
    description = models.TextField()
    publish_date = models.DateTimeField()
    closing_date = models.DateTimeField()

    def __str__(self):
        return self.tender_title
