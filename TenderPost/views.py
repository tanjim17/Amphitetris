from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from User.models import Profile
from .forms import TenderBidForm
from owner.models import Tender
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TenderBid
# Create your views here.


def postview(request):
    all_tenders = Tender.objects.all()
    all_tenders_new = []
    for tenderIns in all_tenders:
        tender = Tender.objects.get(id=tenderIns.id)
        owner = tender.owner
        newData = tenderIns.__dict__
        newData['username'] = str(owner.user.username)
        all_tenders_new.append(newData)
    return render(request, 'mainpost.html', {'post_data': all_tenders_new})


def postdetail(request, pk):
    tender_post = Tender.objects.get(id=pk)
    user_profile = Profile.objects.get(user=request.user)
    message = "Not Applied"
    if TenderBid.objects.filter(tender=tender_post).exists():
        tender_bid = TenderBid.objects.get(tender=tender_post)
        vendor = tender_bid.vendor
    # print(vendor.id)
    # print(user_profile.id)
        if vendor.id == user_profile.id:
            message = "You have already applied for this Tender"
    post_details = tender_post.__dict__
    post_details['cmp_name'] = tender_post.owner.user.username
    post_details['address'] = tender_post.owner.address
    return render(request, 'post_detail.html', {'details': post_details, 'message': message})


def isvendor(request):
    profile = Profile.objects.get(user=request.user)
    if profile.category == 'VR':
        return True
    return False


@login_required
def bidding_form(request, tender_id):
    if isvendor(request):
        if request.method == 'POST':
            form = TenderBidForm(request.POST)
            if form.is_valid():
                newtenderbid = form.save(commit=False)
                newtenderbid.vendor = Profile.objects.get(user=request.user)
                newtenderbid.tender = Tender.objects.get(id=tender_id)
                newtenderbid.save()
                messages.success(request, f'Tender Created!')
                return redirect('tender:tender-post')
        else:
            form = TenderBidForm()
        return render(request, 'biddingForm.html', {'form': form})
    return redirect('login')

