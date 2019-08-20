from django.test import TestCase
from reviews.forms import AddReviewForm


class TestAddAReviewForm(TestCase):

    def test_rating_greater_than_5(self):
        form = AddReviewForm(
            {
             'comments': 'test comment, test comment',
             'rating': '6'}
        )
        self.assertFalse(form.is_valid())

    def test_rating_less_than_1(self):
        form = AddReviewForm(
            {
             'comments': 'test comment, test comment',
             'rating': '0'}
        )
        self.assertFalse(form.is_valid())

    def test_no_comment_left(self):
        form = AddReviewForm(
            {
             'rating': '4'}
        )
        self.assertFalse(form.is_valid())
    
    def test_form_valid_with_comment_rating(self):
        form = AddReviewForm(
            {'comments': 'test comments',
             'rating': '4'}
        )
        self.assertTrue(form.is_valid())