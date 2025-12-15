from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse     # <-- ADD THIS LINE

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", lambda request: JsonResponse({"message": "Ecommerce API is running"})),
    path("admin/", admin.site.urls),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/products/", include("apps.products.urls")),
    path("api/wallet/", include("apps.wallet.urls")),
    path("api/orders/", include("apps.orders.urls")),
]
