from django.conf.urls import url
from . import blog_views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/', blog_views.post_detail, name='post_detail'),
]
