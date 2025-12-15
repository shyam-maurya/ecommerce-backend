from django.db import models
from django.conf import settings
from apps.products.models import Product

class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    product=models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField(default=1)
    total_amount=models.DecimalField(max_digits=12, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20, default='completed')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
