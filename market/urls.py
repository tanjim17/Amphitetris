from django.urls import path, include
from . import views

app_name = 'market'

urlpatterns = [
    path('vendor/', views.showProducts, name="vendorProducts"),
    path('vendor/<int:vendor_id>/<str:product_name>/',
         views.productDetails, name="productDetails"),
    path('emergency', views.emergency, name="emergency")
]

