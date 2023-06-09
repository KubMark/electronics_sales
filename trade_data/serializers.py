from rest_framework import serializers

from trade_data.models import Products, Supplier


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt']
