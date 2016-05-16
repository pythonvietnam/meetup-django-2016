import unittest
from django.test import Client
from django.test import TestCase

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_article_return_hello_world(self):
        response = self.client.get('/article/')

        self.assertEqual(response.status_code, 200)
