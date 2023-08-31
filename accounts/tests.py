from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTest(TestCase):
    username = 'myusername'
    email = 'myusername@gmail.com'

    def test_url_signup(self):
        request = self.client.get(reverse('signup'))
        self.assertEqual(request.status_code, 200)

    def test_name_signup(self):
        request = self.client.get('/accounts/signup/')
        self.assertEqual(request.status_code, 200)

    def test_create_form_signup(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,

        )
        self.assertEqual(get_user_model().objects.all()[0].username, 'myusername')
        self.assertEqual(get_user_model().objects.all()[0].email, 'myusername@gmail.com')
        self.assertEqual(get_user_model().objects.all().count(), 1)









