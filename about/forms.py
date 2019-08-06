from django import forms

class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)