from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from trade_data.filter import SupplierCountryFilter
from trade_data.models import Supplier, Products
from trade_data.permissions import IsActivePermission
from trade_data.serializers import SupplierSerializer, ProductsSerializer


class SupplierCreateView(CreateAPIView):
    model = Supplier
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsActivePermission]


class SupplierListView(ListAPIView):
    model = Supplier
    queryset = Supplier.objects.all()
    permission_classes = [IsActivePermission]
    serializer_class = SupplierSerializer
    filterset_class = SupplierCountryFilter


class SupplierView(RetrieveUpdateDestroyAPIView):
    model = Supplier
    queryset = Supplier.objects.all()
    permission_classes = [IsActivePermission]
    serializer_class = SupplierSerializer


class ProductsCreateView(CreateAPIView):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsActivePermission]


class ProductsListView(ListAPIView):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsActivePermission]


class ProductsView(RetrieveUpdateDestroyAPIView):
    model = Products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsActivePermission]