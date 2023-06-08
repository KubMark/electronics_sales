from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from trade_data.filter import SupplierCountryFilter
from trade_data.models import Supplier
from trade_data.permissions import IsActivePermission
from trade_data.serializers import SupplierSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierCountryFilter
    permission_classes = IsActivePermission
    serializer_class = SupplierSerializer(queryset, many=True)
