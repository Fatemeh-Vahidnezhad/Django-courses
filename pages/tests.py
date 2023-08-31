from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_name_home_page(self):
        request = self.client.get(reverse('home'))
        self.assertEqual(request.status_code, 200)

    def test_url_home_page(self):
        request = self.client.get('/')
        self.assertEqual(request.status_code, 200)

    def test_content_home_page(self):
        request = self.client.get('/')
        self.assertContains(request, 'home')



