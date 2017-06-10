from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent the Post model """
    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date')
