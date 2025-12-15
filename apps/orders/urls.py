from django.urls import path
from .views import PurchaseView, OrderListView

urlpatterns=[
    path('buy/', PurchaseView.as_view()),
    path('my-orders/', OrderListView.as_view()),
]
