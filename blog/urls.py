from django.conf.urls import url
from . import blog_views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/edit/', blog_views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/', blog_views.post_detail, name='post_detail'),
    url(r'^post/new/', blog_views.post_new, name='post_new'),

]
