from django.urls import path
from .views import *

urlpatterns = [
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:vendor_id>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('purchase_orders/', PurchaseOrdersListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:po_id>/', PurchaseOrdersView.as_view(), name='purchase-orders-detail'),
]
