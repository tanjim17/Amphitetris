from django.shortcuts import render, redirect
from vendor.models import Inventory, Orders
from User.models import Profile
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages

# Create your views here.

categories = ['Fiber', 'Fabric', 'Dye', 'Chemical and auxiliaries']


def showProducts(request):
    if request.user.profile.category == "GM":
        products = Inventory.objects.all().exclude(amount=0.0)
        return render(request, 'vendorproducts.html', {'products': products, 'message': "GM", })
    else:
        products = Inventory.objects.filter(~Q(vendor_id=request.user.profile.registration_num)).exclude(amount=0.0)
        return render(request, 'vendorproducts.html', {'products': products})


def productDetails(request, vendor_id, product_name):
    if request.method == "POST":
        userInstance = User.objects.get(username=request.user.username)
        o = Orders(buyer_reg_no=Profile.objects.get(user=userInstance).registration_num, seller_reg_no=vendor_id, product_name=product_name,
                   amount=request.POST['amount'], price=float(Inventory.objects.get(vendor_id=vendor_id, product_name=product_name).price_per_unit) * float(request.POST['amount']))
        o.save()
        messages.success(request, f'Your Purchase Request has been registered!')
        return redirect('market:vendorProducts')
    else:
        product = Inventory.objects.get(
            vendor_id=vendor_id, product_name=product_name)
        vendorInfo = Profile.objects.get(registration_num=vendor_id)
        return render(request, 'productdetails.html', {'product': product, 'vendor': vendorInfo})


def emergency(request):
    if request.method == "POST":
        category = request.POST['Category']
        amount = request.POST['amount']
        date = request.POST['date']

        products = Inventory.objects.filter(category=category).exclude(vendor_id=request.user.profile.registration_num).order_by('amount')
        return render(request, 'showemergency.html', {'products': products})
    else:
        return render(request, 'emergency.html')
