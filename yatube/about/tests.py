from http import HTTPStatus

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    """Тестирование кода ответа статических страниц."""
    def setUp(self):
        self.guest_client = Client()

    def test_about_author_page(self):
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_tech_page(self):
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
