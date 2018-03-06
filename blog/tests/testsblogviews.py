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
        Post.objects.create(author=my_user, title='test post2', text='blablabla', published_date=timezone.now())
        Post.objects.create(author=my_user, title='test post3', text='blablabla', published_date=timezone.now())

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
        resp = self.c.post('/post/new/', {'title': "blabla", 'text': "extra bla"})
        self.assertRedirects(resp, '/post/3/' )

    def test_post_edit(self):
        login = self.c.login(username='testgrace', password='secret')
        post = Post.objects.get(id=2)
        resp = self.c.post('/post/2/edit/', {'post': post})
        self.assertEquals(resp.status_code, 200)

    def test_save_edit(self):
        login = self.c.login(username='testgrace', password='secret')
        testpost = Post.objects.get(id=2)
        self.c.get('/post/2/', {'testpost': testpost})
        resp = self.c.post('/post/2/edit/', {'title': "yellow", 'text': "fafallefafalle", 'published_date': timezone.now()})
        self.assertRedirects(resp, '/post/2/')

#    def test_post_remove(self):
#        login = self.c.login(username='testgrace', password='secret')
#        testpost = Post.objects.get(id=1)
#        self.c.get('/post/1/', {'testpost': testpost})
#        resp = self.c.post('/post/1/remove/', {'testpost': testpost})
#        self.assertRedirects(resp, '/post_list/')
