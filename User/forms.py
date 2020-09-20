from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    registration_num = forms.IntegerField()
    address = forms.CharField()
    category = forms.CharField()

    class Meta:
        model = User  # this form interacts with the model user that is predefined
        fields = ['username', 'email', 'password1', 'password2',
                  'registration_num', 'address', 'category']


# form to update user profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User  # this form interacts with the model user that is predefined
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
