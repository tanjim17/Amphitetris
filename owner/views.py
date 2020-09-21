from django.shortcuts import render, redirect
from owner.forms import TenderForm
from User.models import Profile
from owner.models import *
from TenderPost.models import *
from django.contrib import messages
from datetime import date
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def isOwner(request):
    profile = Profile.objects.get(user=request.user)
    if profile.category == 'GM':
        return True
    return False


@login_required
def createTender(request):
    if isOwner(request):
        if request.method == 'POST':
            form = TenderForm(request.POST)
            if form.is_valid():
                newtender = form.save(commit=False)
                newtender.owner = Profile.objects.get(user=request.user)
                newtender.save()
                messages.success(request, 'Tender Created!')
                return redirect('home:main-page')
        else:
            form = TenderForm()
        return render(request, 'newtender.html', {'form': form})
    return redirect('login')


@login_required
def showTenderDetail(request, tender_id):
    if isOwner(request):
        tender = Tender.objects.get(id=tender_id)
        tenderBids = TenderBid.objects.filter(tender=tender)
        context = {'tender': tender, 'tenderBids': tenderBids,}
        return render(request, 'tenderdetail.html', context)
    return redirect('login')


@login_required
def showBidDetail(request, tender_id, bid_id):
    if isOwner(request):
        tender = Tender.objects.get(id=tender_id)
        bid = TenderBid.objects.get(id=bid_id)
        try:
            order = PurchaseOrder.objects.get(bid=bid)
        except PurchaseOrder.DoesNotExist:
            order = None
        placedOrder = PurchaseOrder.objects.filter(bid__tender=tender).exclude(status=PurchaseOrder.CANCELLED)
        if not placedOrder:
            placed=False
        else:
            placed=True
        context = {'tender': tender, 'bid': bid, 'order': order, 'date': date.today(), 'placed': placed}
        return render(request, 'biddetail.html', context)
    return redirect('login')


@login_required
def deleteTender(request, tender_id):
    if isOwner(request):
        Tender.objects.get(id=tender_id).delete()
        return redirect('home:main-page')
    return redirect('login')


@login_required
def createOrder(request, bid_id):
    if isOwner(request):
        order = PurchaseOrder(bid=TenderBid.objects.get(id=bid_id))
        order.save()
        return redirect('home:main-page')
    return redirect('login')


@login_required
def updateOrder(request, bid_id):
    if isOwner(request):
        order = PurchaseOrder.objects.get(bid=TenderBid.objects.get(id=bid_id))
        order.status = order.SUCCESSFUL
        order.received_date = date.today()
        order.save()
        return redirect('home:main-page')
    return redirect('login')


@login_required
def cancelOrder(request, bid_id):
    if isOwner(request):
        order = PurchaseOrder.objects.get(bid=TenderBid.objects.get(id=bid_id))
        order.status = order.CANCELLED
        print(order.status)
        order.save()
        return redirect('home:main-page')
    return redirect('login')
