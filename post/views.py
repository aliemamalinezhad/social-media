from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category
from rest_framework.permissions import IsAuthenticated


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        srz_data = PostSerializer(instance=posts, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class CreatePostView(APIView):
    def post(self, request, *args, **kwargs):
        data = PostSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status = status.HTTP_201_CREATED)
        return Response(data.errors, status = status.HTTP_400_BAD_REQUEST)


# Create your views here.
