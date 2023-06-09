from django.urls import path
from trade_data import views

urlpatterns = [
    path('supplier/create', views.SupplierCreateView.as_view(), name='create_supplier'),
    path('supplier/list', views.SupplierListView.as_view(), name='list_supplier'),
    path('supplier/<pk>', views.SupplierView.as_view(), name='view_supplier'),

    path('products/create', views.ProductsCreateView.as_view(), name='create_products'),
    path('products/list', views.ProductsListView.as_view(), name='list_products'),
    path('products/<pk>', views.ProductsView.as_view(), name='view_products'),
]
