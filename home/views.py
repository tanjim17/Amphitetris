from django.shortcuts import render
from User.models import Profile
from owner.models import Tender
from datetime import date


def homepage(request):
    profile = Profile.objects.get(user=request.user)
    if profile.category == 'GM':
        tender_list = Tender.objects.filter(owner=profile, closing_date__gte=date.today()).order_by('closing_date')
        context = {'tender_list': tender_list}
        return render(request, 'ownerhome.html', context)
    else:
        return render(request, 'home.html')


def about_page(request):
    return render(request, 'profile.html')

