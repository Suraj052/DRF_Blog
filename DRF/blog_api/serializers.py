from rest_framework import serializers
from blog.models import Post,Category

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title','category', 'author', 'content','imageUrl','published')


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "posts",
        ) 