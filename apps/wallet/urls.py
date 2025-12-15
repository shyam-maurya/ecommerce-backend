from django.urls import path
from .views import WalletDetailView, AddFundsView, TransactionsListView

urlpatterns=[
    path('', WalletDetailView.as_view()),
    path('add-funds/', AddFundsView.as_view()),
    path('transactions/', TransactionsListView.as_view()),
]
