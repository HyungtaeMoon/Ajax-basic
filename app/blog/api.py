from django.urls import re_path
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Post
from .serializers import PostSerializer


class PostPagination(PageNumberPagination):
    page_size = 10


class PostListApiView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPagination


urlpatterns = [
    re_path(r'^posts\.json/$', PostListApiView.as_view(), name='post_list')
]
