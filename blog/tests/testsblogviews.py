from django.test import TestCase
from django.test.client import Client
# Create your tests here.

class BlogViewTest(TestCase):
    c = Client()

    def test_post_detail(self):
        resp = self.c.get('/post/11/')
        self.assertEqual(resp.status_code, 200)
