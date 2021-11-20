from .models import Post, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = ['pk', 'user', 'category', 'caption']

    def create(self, validated_data):
        categories_data = validated_data.pop('category', None)
        post = Post.objects.create(**validated_data)
        category_list = []
        for category_data in categories_data:
            category_id = category_data.pop('pk', None)
            category, _ = Category.objects.get_or_create(id=category_id, defaults=category_data)
            category_list.append(category)

        post.category.add(*category_list)
        return post
