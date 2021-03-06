"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import socket
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
#from rest_framework.routers import DefaultRouter
from blog.blog_views import PostViewSet
from home import home_views #importing views from the home application
from django.contrib.auth import views as auth_views



#if socket.gethostname()=='g-race':
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#if s.bind==("127.0.0.1", 8000):
    #added this if quickly so that I could still view admin page on desktop
#urlpatterns = [
    #url(r'^admin/', admin.site.urls),
#]

#elif s.bind==("127.0.0.1", 8100):
    #this applies to the API
router = routers.DefaultRouter()
router.register(r'api/posts', viewset=PostViewSet)
admin.autodiscover()
#urlpatterns = router.urls
urlpatterns = [
    #url(r'^$', home_views.index, name='home'),
    path('', include('blog.urls')),
    path('', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
