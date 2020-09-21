from django.shortcuts import render, redirect
from .models import Inventory, Orders
from django.contrib.auth.decorators import login_required
from User.models import Profile
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def profile(request):
    return render(request, 'vendorProfile.html')


def purchaseOrders(request):
    return render(request, 'purchaseorders.html')


@login_required
def inventory(request):
    # print(request.user.profile.registration_num)
    # print(request.user.profile.address)
    # print(request.user.profile.category)
    if request.user.profile.category == 'VR':
        porducts = Inventory.objects.filter(
            vendor_id=request.user.profile.registration_num)
        print(porducts)
        return render(request, 'inventory.html', {'products': porducts})

    else:
        return redirect('login')


def sales(request):
    if (request.user.profile.category == "VR"):
        orders = Orders.objects.filter(
            seller_reg_no=request.user.profile.registration_num, accepted='a')
        print(orders)
        return render(request, 'sales.html', {'orders': orders})
    else:
        return redirect('login')


def order(request):
    if request.user.profile.category == "VR":
        orders = Orders.objects.filter(
            seller_reg_no=request.user.profile.registration_num, accepted='p')
        return render(request, "order.html", {'orders': orders})
    else:
        return redirect('login')
    # return render(request, 'order.html')


def vendorInventoryUpdate(vendor_reg, amount, product_name, category, price_per_unit, des):
    try:
        instance = Inventory.objects.get(vendor_id=vendor_reg, product_name = product_name)
        instance.amount = instance.amount + amount
        instance.save()
    except ObjectDoesNotExist:
        product = Inventory(vendor_id=vendor_reg, amount=amount, product_name=product_name,
                            category=category, price_per_unit=price_per_unit, product_description=des)
        product.save()



def orderProcess(request, id, vendor_id, product_name):
    if request.user.profile.category == "VR" and request.user.profile.registration_num == vendor_id:
        if request.method == "POST":
            state = request.POST['state']
            # print(state)
            orderInstance = Orders.objects.get(id=id)
            print("id", id)
            if state == 'accepted':
                orderInstance.accepted = 'a'
            elif state == 'denied':
                orderInstance.accepted = 'd'
            orderInstance.save()
            inventory_u = Inventory.objects.get(vendor_id=vendor_id, product_name=product_name)
            category = inventory_u.category
            price_per_unit = inventory_u.price_per_unit
            des = inventory_u.product_description
            inventory_u.amount = inventory_u.amount - orderInstance.amount
            inventory_u.save()

            if Profile.objects.get(registration_num=orderInstance.buyer_reg_no).category == "VR":
                vendorInventoryUpdate(orderInstance.buyer_reg_no, orderInstance.amount,
                                      product_name, category, price_per_unit, des)

            return redirect('vendor:order')
        else:
            return redirect('vendor:order')

    else:
        return redirect('login')


def editProduct(request, product_name):
    print(product_name)
    if request.method == 'POST':
        amount = request.POST['amount']
        price_per_unit = request.POST['price_per_unit']
        description = request.POST['description']
        category = request.POST['Category']
        print(price_per_unit, description, category, amount)

        products = Inventory.objects.get(
            vendor_id=request.user.profile.registration_num,
            product_name=product_name)
        products.amount = amount
        products.category = category
        products.price_per_unit = price_per_unit
        products.product_description = description
        products.save()

        return redirect('vendor:inventory')

    else:
        product = Inventory.objects.get(
            vendor_id=request.user.profile.registration_num,
            product_name=product_name)
        pr = None
        # for p in product:
        #     print(p.amount)
        #     pr = p
        return render(request, 'editForm.html', {'product_name': product_name, 'product': product})


def addProduct(request):
    print('mairala')
    if request.method == 'POST':
        product_name = request.POST['porduct_name']
        amount = request.POST['amount']
        price_per_unit = request.POST['price_per_unit']
        description = request.POST['description']
        category = request.POST['Category']
        print(product_name, amount, price_per_unit, description, category)

        if Inventory.objects.filter(vendor_id=request.user.profile.registration_num, product_name=product_name):
            return render(request, 'addproduct.html', {'message': 'This product already exists'})
        else:
            product = Inventory()
            product.vendor_id = request.user.profile.registration_num
            product.product_name = product_name
            product.amount = amount
            product.category = category
            product.price_per_unit = price_per_unit
            product.product_description = description
            product.save()

            return redirect('vendor:inventory')
    else:
        return render(request, 'addproduct.html')


def allProducts(request):
    return render(request, 'products.html')


def notification(request):
    return render(request, 'notification.html')