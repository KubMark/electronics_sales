import django_filters

from trade_data.models import Supplier


class SupplierCountryFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name='supplier__country')

    class Meta:
        model = Supplier
        fields = ('country', )
