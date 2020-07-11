from __future__ import unicode_literals

from django.db import models

class AccountHistory(models.Model):
    id = models.IntergerField(primary_key=True)
    Timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    Category = models.CharField(max_length=50)
    Money = models.DecimalField(max_digits=10, decimal_places=2)
    Descriptions = models.CharField(max_length=50)
