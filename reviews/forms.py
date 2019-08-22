from django import forms
from reviews.models import Review

# creates a form for a new review
class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comments','rating')
        labels = {
           "rating": "Rate our service out of 5"
    }