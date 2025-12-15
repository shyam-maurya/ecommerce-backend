from decimal import Decimal
from django.db import transaction
from django.contrib.auth import get_user_model
from .models import Wallet, Transaction

User=get_user_model()

class WalletServiceError(Exception):
    pass

class WalletService:

    @staticmethod
    def get_or_create_wallet(user):
        w, _ = Wallet.objects.get_or_create(user=user)
        return w

    @staticmethod
    @transaction.atomic
    def credit(user, amount, description=""):
        amount=Decimal(amount)
        if amount<=0: raise WalletServiceError("Amount must be positive")
        w=WalletService.get_or_create_wallet(user)
        w.balance += amount
        w.save(update_fields=['balance'])
        return Transaction.objects.create(
            wallet=w, transaction_type=Transaction.CREDIT,
            amount=amount, balance_after_transaction=w.balance,
            description=description
        )

    @staticmethod
    @transaction.atomic
    def debit(user, amount, description=""):
        amount=Decimal(amount)
        w=WalletService.get_or_create_wallet(user)
        if amount<=0: raise WalletServiceError("Amount must be positive")
        if w.balance < amount: raise WalletServiceError("Insufficient balance")
        w.balance -= amount
        w.save(update_fields=['balance'])
        return Transaction.objects.create(
            wallet=w, transaction_type=Transaction.DEBIT,
            amount=amount, balance_after_transaction=w.balance,
            description=description
        )
