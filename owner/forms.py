from django import forms
from owner.models import Tender
from User.models import Profile
from django.contrib.auth.models import User

class TenderForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects)

    class Meta:
        model = Tender
        fields = ['tender_title', 'product_name', 'amount', 'category',
                  'description', 'publish_date', 'closing_date']
        widgets = {
            'publish_date': forms.DateInput(format=('%m/%d/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'closing_date': forms.DateInput(format=('%m/%d/%Y'),
                                            attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                   'type': 'date'}),
        }
