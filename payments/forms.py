from django import forms
from payments.models import SingleOrder


class SinglePayForm(forms.Form):

    MONTHS = [(i, i) for i in range(1, 13)]
    YEARS = [(i, i) for i in range(2019, 2030)]

    card_number = forms.CharField(label="Your Card Number", required=False)
    cvv = forms.CharField(label="Security Number", required=False)
    expiry_month = forms.ChoiceField(
        label="Expiry Month", choices=MONTHS, required=False)
    expiry_year = forms.ChoiceField(
        label="Expiry Year", choices=YEARS, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class SingleOrderForm(forms.ModelForm):
    class Meta:
        model = SingleOrder
        fields = ('name', 'contact_number', 'address1', 'address2',
                  'town', 'county', 'postcode', 'country', 'brief')


# class BriefForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('brief',)