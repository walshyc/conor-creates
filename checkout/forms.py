from django import forms
from checkout.models import Order

class PayForm(forms.Form):

    MONTHS = [(i, i) for i in range(1, 12)]
    YEARS = [(i, i) for i in range(2019,2030)]

    card_number = forms.CharField(label = "Your Card Number", required = False)
    cvv = forms.CharField(label = "Security Number", required = False)
    expiry_month = forms.ChoiceField(label = "Expiry Month", choices = MONTHS, required = False)
    expiry_year = forms.ChoiceField(label = "Expiry Year", choices = YEARS, required = False)
    stripe_id = forms.CharField(widget = forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('name','contact_number', 'address1', 'address2', 'town', 'county', 'postcode' ,'country' )
