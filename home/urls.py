from django.urls import path
from . import home_views

urlpatterns = [
    path('', home_views.index, name='home'),
    path('post_list/', home_views.post_list, name='post_list'),
]
