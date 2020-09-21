from django.urls import path, include
from . import views

app_name = 'vendor'


urlpatterns = [
    path('', views.profile, name='Profile'),
    path('accounts/', views.purchaseOrders, name='purchaseorders'),
    path('inventory/', views.inventory, name='inventory'),
    path('sales/', views.sales, name='sales'),
    path('order/', views.order, name='order'),
    path('order/<int:id>/<int:vendor_id>/<str:product_name>/',
         views.orderProcess, name="orderProcess"),
    path('inventory/<str:product_name>/',
         views.editProduct, name='edit_product'),
    path('inventory/add_product', views.addProduct, name='addProduct'),
    path('notification/', views.notification, name='vendor_noti'),
]
