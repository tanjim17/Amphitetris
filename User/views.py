from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.


def test_index(request):
    return render(request, 'User/test_index.html')


def saveProfileInfo(userRegData):
    # print(userRegData)

    # profile = Profile()
    # profile.category = userRegData['category']
    # profile.address = userRegData['address']
    # profile.registration_num = userRegData['registration_num']
    # profile.save()
    userName = userRegData['username']
    userInstance = User.objects.get(username=userName)
    profile = Profile.objects.get(user=userInstance)
    print(profile)
    profile.category = userRegData['category']
    profile.address = userRegData['address']
    profile.registration_num = userRegData['registration_num']
    profile.save()


def register(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['registration_num'])
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            saveProfileInfo(request.POST)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your user account has been updated!')
            return redirect('user:profile')
            # post get redirect pattern
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    if(request.user.profile.category == 'VR'):
        return render(request, 'vendorProfile.html', context)
