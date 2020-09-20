from django.shortcuts import render, redirect
from .models import Inventory
from django.contrib.auth.decorators import login_required

# Create your views here.


def profile(request):
    return render(request, 'vendorProfile.html')


def accounts(request):
    return render(request, 'accounts.html')


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
    return render(request, 'sales.html')


def order(request):
    return render(request, 'order.html')


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
        for p in product:
            print(p.amount)
            pr = p
        return render(request, 'editForm.html', {'product_name': product_name, 'product': pr})


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
