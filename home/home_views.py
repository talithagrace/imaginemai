from django.template import RequestContext
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    return render(request,'home/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
