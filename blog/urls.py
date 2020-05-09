from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import blog_views

urlpatterns = [
    path('post/<int:pk>/edit/', blog_views.post_edit, name='post_edit'),
    path('post/<int:pk/remove/', blog_views.post_remove, name='post_remove'),
    path('post/<int:pk>/', blog_views.post_detail, name='post_detail'),
    path('post/new/', blog_views.post_new, name='post_new'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
