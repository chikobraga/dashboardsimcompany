from __future__ import unicode_literals

from django.db import models

class AccountHistory(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=True)
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    Category = models.CharField(max_length=50)
    Money = models.DecimalField(max_digits=10, decimal_places=2)
    Descriptions = models.CharField(max_length=50)

class Details(models.Model):
    Accountid = models.ForeignKey(AccountHistory, related_name='id_account', null=True, blank=True, on_delete=models.CASCADE)
    Resource = models.CharField(max_length=50)
    Amount = models.IntegerField()
    Quality = models.CharField(max_length=50)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Buyer = models.CharField(max_length=50, null=True, blank=True)
    Profit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)