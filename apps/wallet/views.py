from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from decimal import Decimal
from .models import Wallet
from .serializers import WalletSerializer, TransactionSerializer
from .services import WalletService, WalletServiceError

class WalletDetailView(generics.RetrieveAPIView):
    serializer_class=WalletSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        w,_=Wallet.objects.get_or_create(user=self.request.user)
        return w

class AddFundsView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def post(self, request):
        amt=request.data.get('amount')
        try:
            amt=Decimal(str(amt))
        except:
            return Response({"detail":"Invalid amount"}, status=400)
        try:
            tx=WalletService.credit(request.user, amt, "Wallet top-up")
            return Response({"detail":"credited","tx":tx.id})
        except WalletServiceError as e:
            return Response({"detail":str(e)}, status=400)

class TransactionsListView(generics.ListAPIView):
    serializer_class=TransactionSerializer
    permission_classes=[permissions.IsAuthenticated]
    def get_queryset(self):
        w,_=Wallet.objects.get_or_create(user=self.request.user)
        return w.transactions.all()
