from django.shortcuts import render
from User.models import Profile
from owner.models import Tender
from TenderPost.models import *
from datetime import date


def homepage(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if profile.category == 'GM':
            tender_list = Tender.objects.filter(owner=profile, closing_date__gte=date.today()).order_by('closing_date')
            orders = PurchaseOrder.objects.filter(bid__tender__owner=profile)
            context = {'tender_list': tender_list, 'orders': orders}
            return render(request, 'ownerhome.html', context)
        else:
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')


def about_page(request):
    return render(request, 'profile.html')