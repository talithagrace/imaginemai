from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import blog_views

urlpatterns = [
    url(r'^post/(?P<pk>\d+)/edit/', blog_views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/', blog_views.post_detail, name='post_detail'),
    url(r'^post/new/', blog_views.post_new, name='post_new'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
