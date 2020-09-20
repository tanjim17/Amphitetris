from django import forms
from owner.models import Tender


class TenderForm(forms.ModelForm):
    class Meta:
        model = Tender
        fields = ['tender_title', 'product_name', 'amount', 'category',
                  'description', 'publish_date', 'closing_date']
        widgets = {
            'publish_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }
