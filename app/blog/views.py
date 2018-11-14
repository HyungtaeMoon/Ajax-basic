from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from .models import Post

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_create = CreateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')


# post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:index'))

# 위의 post_delete CBV 를 아래와 같이 상속받아 가독성을 높일 수 있다.
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')


post_delete = PostDeleteView.as_view()
