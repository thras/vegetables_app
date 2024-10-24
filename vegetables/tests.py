from django.test import TestCase
from django.urls import reverse
from .models import Vegetable
from django.contrib.auth import get_user_model

# Create your tests here.
class VegetableTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="dummyUser",
            email="dummyUser@email.com",
            password="test1234"
        )
        
        cls.vegetable = Vegetable.objects.create(
            name = "Tomato",
            calorie = "13",
            kilojoule = "137",
            category = "Fruit",
            wiki = "www.testurl.com",
        )

    def test_vegetable_listing(self):
        self.assertEqual(f"{self.vegetable.name}", "Tomato")
        self.assertEqual(f"{self.vegetable.calorie}", "13")
        self.assertEqual(f"{self.vegetable.kilojoule}", "137")
        self.assertEqual(f"{self.vegetable.category}", "Fruit")
        self.assertEqual(f"{self.vegetable.wiki}", "www.testurl.com")

    def test_vegetable_list_view_login(self):
        self.client.login(username="dummyUser", password="test1234")
        response = self.client.get(reverse("vegetable_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Tomato")
        self.assertTemplateUsed(response, "vegetables/vegetable_list.html")

    def test_vegetable_list_view_logout(self):
        self.client.logout()
        response = self.client.get(reverse("vegetable_list"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
        response, "%s?next=/vegetables/" % (reverse("login")))
        response = self.client.get("%s?next=/vegetables/" % (reverse("login")))
        self.assertContains(response, "Log In")       

    def test_vegetable_detail_view(self):
        self.client.login(username="dummyUser", password="test1234")
        response = self.client.get(self.vegetable.get_absolute_url())
        no_response = self.client.get("/vegetables/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Tomato")
        self.assertTemplateUsed(response, "vegetables/vegetable_detail.html")
       