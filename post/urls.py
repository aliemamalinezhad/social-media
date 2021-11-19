from django.urls import path, include
from . import views

app_name = 'post'

api_urls = [
    path('posts/', views.PostListView.as_view(), name='posts'),
]

urlpatterns = [
    path('api/', include('api_urls')),
]
