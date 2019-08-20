from django import forms
from reviews.models import Review

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comments')