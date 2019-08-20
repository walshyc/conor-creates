from django.shortcuts import render, get_object_or_404, reverse, redirect
from reviews.models import Review
from reviews.forms import AddReviewForm
from services.models import Service
from django.contrib import messages
from django.utils import timezone

def new_review(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        review_form = AddReviewForm(request.POST)
        
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.date = timezone.now()
            review.user = request.user
            review.service = get_object_or_404(Service, pk=pk)
            review.save()
                           
            return redirect(reverse('index'))
         

        else:
            messages.error(request, "Forms did not validate")

    else:
        review_form = AddReviewForm()
        

    return render(request, 'review.html', {'service': service, 'review_form': review_form})
