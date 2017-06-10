from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from blog.models import Post
from blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
