from django.db import models
from django.conf import settings
from decimal import Decimal

class Wallet(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='wallet')
    balance=models.DecimalField(max_digits=12, decimal_places=2, default=Decimal('0.00'))

    def __str__(self):
        return f"{self.user.username} wallet"

class Transaction(models.Model):
    CREDIT='credit'
    DEBIT='debit'
    TYPE_CHOICES=[(CREDIT,'Credit'),(DEBIT,'Debit')]

    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,related_name='transactions')
    transaction_type=models.CharField(max_length=10,choices=TYPE_CHOICES)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    balance_after_transaction=models.DecimalField(max_digits=12,decimal_places=2)
    timestamp=models.DateTimeField(auto_now_add=True)
    description=models.TextField(blank=True)

    class Meta:
        ordering=['-timestamp']
