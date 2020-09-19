from django.shortcuts import render, redirect
from owner.forms import TenderForm
from django.contrib import messages


def ownerhome(request):
    return render(request, 'ownerhome.html')


def createTender(request):
    if request.method == 'POST':
        form = TenderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Tender Created!')
            return redirect('owner:ownerhome')
    else:
        form = TenderForm()
    return render(request, 'newtender.html', {'form': form})

