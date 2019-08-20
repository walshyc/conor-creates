from django import forms
from reviews.models import Review

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comments','rating')
        labels = {
           "rating": "Rate our service out of 5"
    }