from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from blog.models import Post
from blog.serializers import PostSerializer
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

class PostViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
