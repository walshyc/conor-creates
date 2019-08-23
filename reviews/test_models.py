from django.test import TestCase
from reviews.models import Review
from services.models import Service
from django.contrib.auth.models import User
from django.utils import timezone


class TestReviewModel(TestCase):

    def test_create_review(self):
        service = Service(name="Test Service for review",
                          description="Test description service review",
                          price=29)

        review = Review(service=service, date=timezone.now(),
                        comments="test review", rating=4)
        self.assertEqual(review.service.name, "Test Service for review")
        self.assertEqual(review.comments, "test review")
        self.assertEqual(review.rating, 4)
        self.assertFalse(review.approved)

