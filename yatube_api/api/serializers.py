from django.contrib.auth import get_user_model
from rest_framework import serializers

from posts.models import Comment, Group, Post

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "author", "text", "pub_date", "image", "group")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.IntegerField(source='post.id', read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "author", "post", "text", "created")
        # read_only_fields = ("post",)
