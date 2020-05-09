from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone


# Create your tests here.
class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #set up non-modified objects used by all test methods
        my_user = User.objects.create_user(username='testgrace', email='testgrace@grace.com', password='secret')
        image_path = r'''C:\\Users\\grace\\Documents\\portfolioimage.png'''
        my_image = SimpleUploadedFile(name='portfolioimage.png', content=open(image_path, 'rb').read(), content_type='image/png')
        Post.objects.create(author=my_user, title='test post', text='blablabla', pic=my_image, published_date=timezone.now())
        Post.objects.create(author=my_user, title='test post3', text='blablabla', published_date=timezone.now())

    def test_title_max_length(self):
        post=Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)
        #self.assertEquals(max_length, 100)

    def test_image_upload(self):
        post=Post.objects.get(id=1)
        upload_to = post._meta.get_field('pic').upload_to
        self.assertEquals(upload_to, 'images/')
