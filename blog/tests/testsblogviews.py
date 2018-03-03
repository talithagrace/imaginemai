from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone
# Create your tests here.

class BlogViewTest(TestCase):

    c = Client()

    @classmethod
    def setUpTestData(cls):
        my_user = User.objects.create_user(username='testgrace', email='testgrace@grace.com', password='secret')
        Post.objects.create(author=my_user, title='test post', text='blablabla', published_date=timezone.now())
        #testpost.save()

    def test_post_detail(self):
        resp = self.c.get('/post/1/')
        self.assertEqual(resp.status_code, 200)

    def test_post_new(self):
        login = self.c.login(username='testgrace', password='secret')
        form = PostForm()
        resp = self.c.post('/post/new/', {'form': form})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/post_edit.html')

    def test_post_save(self):
        login = self.c.login(username='testgrace', password='secret')
        #testpost = PostForm(data={'title': "blabla", 'text': "extra bla"})
        resp = self.c.post('/post/new/', {'title': "blabla", 'text': "extra bla"})
        self.assertRedirects(resp, '/post/2/' )
