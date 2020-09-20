from django import forms
from TenderPost.models import TenderBid


class TenderBidForm(forms.ModelForm):
    class Meta:
        model = TenderBid
        fields = ['price', 'amount', 'product_description', 'delivery_date']
        widgets = {
            'delivery_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }