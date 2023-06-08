from django.urls import path, include
from rest_framework.routers import SimpleRouter
from trade_data.views import SupplierViewSet

supplier_router = SimpleRouter()
supplier_router.register('supplier', SupplierViewSet, basename='supplier')

urlpatterns = [
    path('', include(supplier_router.urls)),
]
