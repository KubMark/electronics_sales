from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from trade_data.models import Supplier, Products


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('title', 'types', 'debt', 'create_date', 'provider_link')
    list_filter = ('supplier__city',)
    fieldsets = [
        (None, {'fields': ['title', 'types', 'provider', 'debt']}),
        ('Контактная информация', {'fields': ['email', 'country', 'city', 'street', 'building_number']})
    ]

    def provider_link(self, obj):
        """ Provider link """
        if obj.provider:
            url = reverse('admin:trade_data_supplier_change', args=(obj.provider.id,))
            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.provider))

    actions = ['debt_clear']
    """ Function to clear debt """
    @admin.action(description='Clear Debt')
    def debt_clear(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Products)
