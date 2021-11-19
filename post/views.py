from django.shortcuts import render, redirect
from rest_framework.views import APIView
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Category
from rest_framework.permissions import IsAuthenticated


class PostListView(APIView):
    pass

# Create your views here.
