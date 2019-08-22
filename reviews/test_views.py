from django.test import TestCase
from reviews.models import Review
from reviews.forms import AddReviewForm
from django.utils import timezone
from services.models import Service

class TestReviewsViews(TestCase):

    def test_get_new_review(self):
        service = Service.objects.create(name="test service", description = "test service description", price = "100", main_image= "test_image.jpg", short = "testshort")
        review = Review.objects.create(comments='Test Discussion Post',
                                   rating='1',date = timezone.now(), service = service)
        
        review.save()

        page = self.client.get('/reviews/{0}'.format(review.id))
        self.assertEqual(page.status_code,301)
        
