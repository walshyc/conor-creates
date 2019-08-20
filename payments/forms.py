from django import forms
from django.forms.widgets import TextInput
from payments.models import SingleOrder


class SinglePayForm(forms.Form):

    MONTHS = [(i, i) for i in range(1, 13)]
    YEARS = [(i, i) for i in range(2019, 2030)]

    card_number = forms.CharField(label="Your Card Number", required=False, max_length=16, min_length=16)
    cvv = forms.CharField(label="Security Number", required=False, max_length=3, min_length=3)
    expiry_month = forms.ChoiceField(
        label="Expiry Month", choices=MONTHS, required=False)
    expiry_year = forms.ChoiceField(
        label="Expiry Year", choices=YEARS, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


class SingleOrderForm(forms.ModelForm):
    class Meta:
        model = SingleOrder
        fields = ('name', 'contact_number', 'email', 'primary_color', 'secondary_color', 'brief')
        labels = {
           "primary_color": "Main Color",
           "secondary_color": "Other Color"
    }
        widgets = {
            'brief': forms.Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'Enter as much detail as possbile about how you would like you design to look'}),
            'primary_color': TextInput(attrs={'type': 'color'}),
            'secondary_color': TextInput(attrs={'type': 'color'}),
        }



        


# class BriefForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ('brief',)
