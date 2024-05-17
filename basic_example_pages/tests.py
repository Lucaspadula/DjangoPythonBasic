from django.test import SimpleTestCase,TestCase
from django.urls import reverse
from .models import *


class AboutPageTest(SimpleTestCase):
    def test_url_exists_ar_correct_location(self):
        response = self.client.get("/about/")

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")
        
    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<p>this is the About page</p>")
        
        

class ContactPageTest(SimpleTestCase):
    def test_url_exists_ar_correct_location(self):
        response = self.client.get("/contact/")

    def test_url_available_by_name(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        
    def test_template_name_correct(self):
        response = self.client.get(reverse("contact"))
        self.assertTemplateUsed(response, "contact.html")
        
    def test_template_content(self):
        response = self.client.get(reverse("contact"))
        self.assertContains(response, "<p>this is the contact page</p>")
        

class BookAuthorTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.autor = BookAuthor.objects.create(
            name="Leonel Messi",
            country = "Argentina")
    
    def test_model_content(self):
        self.assertEqual(self.autor.name, "Leonel Messi")