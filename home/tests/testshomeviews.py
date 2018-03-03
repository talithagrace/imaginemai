from django.test import TestCase
from django.test.client import Client

# Create your tests here.

class HomeViewsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        c = Client()


    def test_index(self):
        resp = self.c.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home/index.html')

    def test_post_list(self):
        resp = self.c.get('/post_list/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/post_list.html')
