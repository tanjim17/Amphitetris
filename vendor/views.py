from django.shortcuts import render
from .models import Inventory

# Create your views here.


def profile(request):
    return render(request, 'vendorProfile.html')


def accounts(request):
    return render(request, 'accounts.html')


def inventory(request):
    porducts = Inventory.objects.filter(vendor_id=10000)
    return render(request, 'inventory.html')


def sales(request):
    return render(request, 'sales.html')


def order(request):
    return render(request, 'order.html')
