from blog.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    username  = serializers.SerializerMethodField('get_username_from_user')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'url', 'updated', 'username']

    def get_username_from_user(self, Post):
        username = Post.author.username
        return username

