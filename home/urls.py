from django.conf.urls import url
from . import home_views

urlpatterns = [
    url(r'^$', home_views.index, name='home'),
    url(r'^post_list/', home_views.post_list, name='post_list'),
]
