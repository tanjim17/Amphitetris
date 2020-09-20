from django.shortcuts import render
from User.models import Profile


def homepage(request):
    if Profile.objects.get(user=request.user).category == 'GM':
        return render(request, 'ownerhome.html')
    else:
        return render(request, 'home.html')


def about_page(request):
    return render(request, 'profile.html')