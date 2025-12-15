from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import PurchaseSerializer, OrderSerializer
from .services import PurchaseService, PurchaseError
from .models import Order

class PurchaseView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        s=PurchaseSerializer(data=request.data)
        s.is_valid(raise_exception=True)
        try:
            order=PurchaseService.purchase_product(
                request.user,
                s.validated_data['product_id'],
                s.validated_data.get('quantity',1)
            )
            return Response({"detail":"success","order":order.id})
        except PurchaseError as e:
            return Response({"detail":str(e)}, status=400)

class OrderListView(generics.ListAPIView):
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).order_by('-created_at')
