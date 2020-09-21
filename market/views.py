from django.shortcuts import render, redirect
from vendor.models import Inventory, Orders
from User.models import Profile
from django.contrib.auth.models import User

# Create your views here.

categories = ['Fiber', 'Fabric', 'Dye', 'Chemical and auxiliaries']


def showProducts(request):
    products = Inventory.objects.all()
    print(products)
    return render(request, 'vendorproducts.html', {'products': products})


def productDetails(request, vendor_id, product_name):
    if request.user.profile.category == "GM":
        if (request.method == "POST"):
            userInstance = User.objects.get(username=request.user.username)
            o = Orders(buyer_reg_no=Profile.objects.get(user=userInstance).registration_num, seller_reg_no=vendor_id, product_name=product_name,
                       amount=request.POST['amount'], price=float(Inventory.objects.get(vendor_id=vendor_id, product_name=product_name).price_per_unit) * float(request.POST['amount']))
            o.save()

            return redirect('market:vendorProducts')
        else:
            product = Inventory.objects.get(
                vendor_id=vendor_id, product_name=product_name)
            vendorInfo = Profile.objects.get(registration_num=vendor_id)
            return render(request, 'productdetails.html', {'product': product, 'vendor': vendorInfo})
    else:
        return showProducts(request)
