from rest_framework import serializers

from trade_data.models import Contacts, Products, Supplier


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductsSerializer(many=True, read_only=True)
    contacts = ProductsSerializer(read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['debt']
