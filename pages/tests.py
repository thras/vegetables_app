from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


# Create your tests here.
class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_pass_html(self):
        self.assertContains(self.response, 'Home')
    
    def test_homepage_fail_html(self):
        self.assertNotContains(self.response, 'Just fail') 

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)