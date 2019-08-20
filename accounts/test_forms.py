from django.test import TestCase
from accounts.forms import UserLoginForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.models import User


class TestLoginForm(TestCase):

    def test_login_password_required(self):
        form = UserLoginForm(
            {'username': 'test'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_login_username_required(self):
        form = UserLoginForm(
            {'password': 'testpassword'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])


class TestRegisterForm(TestCase):

    def test_email_is_unique(self):
        User.objects.create_user(
            username='testusername',
            email='test@test.com')

        form = UserRegisterForm(
            {'username': 'test',
             'email': 'test@test.com',
             'password1': 'testpassword',
             'password2': 'testpassword'})
        self.assertFalse(form.is_valid())

    def test_register_password_must_match(self):
        form = UserRegisterForm(
            {'username': 'test',
             'email': 'test@test.com',
             'password1': 'testpassword',
             'password2': 'testpassword1'}
        )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [
                         'Passwords must be the same'])

    def test_register_password_matches(self):
        form = UserRegisterForm(
            {'username': 'test',
             'email': 'test@test.com',
             'password1': 'testpassword',
             'password2': 'testpassword'}
        )
        self.assertTrue(form.is_valid())


class TestUserUpdateForm(TestCase):

    def test_no_email(self):
        User.objects.create_user(
            username='testusername',
            email='test@test.com')

        form = UserUpdateForm(
            {'username': 'testuser'}
           )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'This field is required.'])

    def test_no_username(self):
        User.objects.create_user(
            username='testusername',
            email='test@test.com')

        form = UserUpdateForm(
            {'email': 'test@test.com'}
           )
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [
                         'This field is required.'])

        
    
