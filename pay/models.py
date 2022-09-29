from django.db import models

# Create your models here.
from django.db import models


class Transaction(models.Model):
    amount = models.DecimalField(default=.0, decimal_places=2, max_digits=9)
    description = models.TextField(verbose_name='description')
    # salt = models.CharField(max_length=25, verbose_name='salt')

