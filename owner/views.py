from django.shortcuts import render, redirect
from owner.forms import TenderForm
from User.models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def isOwner(request):
    profile = Profile.objects.get(user=request.user)
    print(profile.category)
    if profile.category == 'GM':
        return True
    return False


@login_required
def ownerhome(request):
    if isOwner(request):
        return render(request, 'ownerhome.html')
    return redirect('login')


@login_required
def createTender(request):
    if isOwner(request):
        if request.method == 'POST':
            form = TenderForm(request.POST)
            if form.is_valid():
                newtender = form.save(commit=False)
                newtender.owner = Profile.objects.get(user=request.user)
                newtender.save()
                messages.success(request, f'Tender Created!')
                return redirect('owner:ownerhome')
        else:
            form = TenderForm()
        return render(request, 'newtender.html', {'form': form})
    return redirect('login')
