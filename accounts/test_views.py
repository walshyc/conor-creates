from django.test import TestCase
from django.contrib.auth.models import User, AnonymousUser

class TestAccountsViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get('/')
        self.assertEqual(page.status_code,200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_get_login_page(self):
        page = self.client.get('/accounts/login/')
        self.assertEqual(page.status_code,200)
        self.assertTemplateUsed(page, "login.html")
    
    def test_get_register_page(self):
        page = self.client.get('/accounts/register/')
        self.assertEqual(page.status_code,200)
        self.assertTemplateUsed(page, "register.html")

    def test_user_log_in(self):
        user1 = User.objects.create_user(

            username='testusername',
            email='test@test.com',
            password='password'
            )

        response = self.client.get('/')

        self.assertEqual(response.context['user'], AnonymousUser())


    def test_register_user(self):
        
        self.assertEqual(User.objects.count(),0)

        new_user = self.client.post("/accounts/register/", {
            'username': 'newtestuser',
            'email': 'newtest@test.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })    

        self.assertEqual(new_user.status_code, 302)
        self.assertRedirects(new_user, '/')

        self.assertEqual(User.objects.count(),1)

    def test_register_form_invalid_does_not_register_new_user(self):
        new_user_two = self.client.post("/accounts/register/", {
            'username': 'newtestuser',
            'email': 'newtesttest.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })    


        self.assertEqual(User.objects.count(),0)
     
        