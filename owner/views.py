from django.shortcuts import render, redirect
from owner.forms import TenderForm
from User.models import Profile
from owner.models import Tender
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
        context = {'tender': tender}
        return render(request, 'tenderdetail.html', context)
    return redirect('login')


@login_required
def deleteTender(request, tender_id):
    if isOwner(request):
        Tender.objects.get(id=tender_id).delete()
        return redirect('home:main-page')
    return redirect('login')

