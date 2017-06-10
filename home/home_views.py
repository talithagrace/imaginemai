from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request,'home/index.html', {})
