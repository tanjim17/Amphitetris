from django.shortcuts import render


def ownerhome(request):
    return render(request, 'ownerhome.html')
