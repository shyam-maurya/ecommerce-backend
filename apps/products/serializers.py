from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        read_only_fields=('created_at','updated_at')

    def validate_price(self, v):
        if v<=0: raise serializers.ValidationError("Price must be positive")
        return v

    def validate_stock_quantity(self, v):
        if v<0: raise serializers.ValidationError("Stock cannot be negative")
        return v
