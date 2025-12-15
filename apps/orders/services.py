from decimal import Decimal
from django.db import transaction
from apps.products.models import Product
from apps.wallet.services import WalletService, WalletServiceError
from .models import Order

class PurchaseError(Exception):
    pass

class PurchaseService:
    @staticmethod
    @transaction.atomic
    def purchase_product(user, product_id, quantity=1):
        if quantity<=0:
            raise PurchaseError("Quantity must be positive")

        try:
            product=Product.objects.select_for_update().get(pk=product_id)
        except Product.DoesNotExist:
            raise PurchaseError("Product not found")

        if product.stock_quantity < quantity:
            raise PurchaseError("Insufficient stock")

        total=(product.price * Decimal(quantity)).quantize(Decimal('0.01'))

        try:
            WalletService.debit(user, total, f"Purchase {product.name} x{quantity}")
        except WalletServiceError as e:
            raise PurchaseError(str(e))

        product.stock_quantity -= quantity
        product.save(update_fields=['stock_quantity'])

        return Order.objects.create(
            user=user, product=product,
            quantity=quantity, total_amount=total
        )
