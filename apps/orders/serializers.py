from rest_framework import serializers
from .models import Order

class PurchaseSerializer(serializers.Serializer):
    product_id=serializers.IntegerField()
    quantity=serializers.IntegerField(default=1)

class OrderSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')

    class Meta:
        model=Order
        fields=('id','product','product_name','quantity','total_amount','created_at','status')
