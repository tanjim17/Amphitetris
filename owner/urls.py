from django.urls import path
from . import views

app_name = 'owner'

urlpatterns = [
    path('newtender/', views.createTender, name='newtender'),
    path('tender/<int:tender_id>/', views.showTenderDetail, name='showtender'),
    path('deleted/<int:tender_id>/', views.deleteTender, name='deletetender'),
    path('tender/<int:tender_id>/bid/<int:bid_id>/', views.showBidDetail, name='showbid'),
    path('ordered/<int:bid_id>/', views.createOrder, name='createorder'),
]