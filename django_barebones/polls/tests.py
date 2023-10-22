from django.test import TestCase
from django.urls import reverse

class IndexViewTests(TestCase):
    def test_index_view_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_returns_expected_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, '<h1>Simple Django Website</h1>')
        self.assertContains(response, '<p>Just saying hello</p>')
        self.assertContains(response, '<a href=" admin/">Admin Site</a>')