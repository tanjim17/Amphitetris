from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from User.models import Profile
from .forms import TenderBidForm
from owner.models import Tender
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def postview(request):
    content = {
        'id': 40,
        'name': 'J&Kenterprise',
        'tenderno': 45,
        'tendertitle': 'need clothes',
        'publish_date': '25/9/20',
        'closing_date': '30/9/20',
        'description': 'Need superior quality linen',
        'category': 'clothes',
    }

    all_tenders = Tender.objects.all()

    return render(request, 'mainpost.html', {'post_data': all_tenders})


def postdetail(request, pk):
    post_details = {
        'id': pk,
        'cmp_name': "J&Kenterprise",
        'address': "mirpur",
        'tendertitle': 'need clothes',
        'publish_date': '25/9/20',
        'closing_date': '30/9/20',
        'description': 'Need superior quality linen',
        'category': 'clothes',
    }
    return render(request, 'post_detail.html', {'details': post_details})


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

