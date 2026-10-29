from django.test import TestCase
from django.urls import reverse

class HelloAPITests(TestCase):

    def test_hello_status(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)

    def test_hello_message(self):
        response = self.client.get(reverse('hello'))
        self.assertEqual(
            response.json()['message'],
            'Hello from CSC 325!'
        )