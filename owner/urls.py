from django.urls import path
from . import views

app_name='owner'

urlpatterns = [
    path('', views.ownerhome, name='ownerhome'),
    path('newtender/', views.createTender, name='newtender'),
]