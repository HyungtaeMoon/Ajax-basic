from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_detail = DetailView.as_view(model=Post)

# def post_detail(request, pk):
#     '''
#     post_detail의 FBV 이며, Post DB 에서
#     pk 값에 해당하는 객체만을 불러와서 뿌려준다.
#     '''
#     post = Post.objects.filter(pk=pk)
#     context = {
#         'post': post,
#     }
#     return render(request, 'blog/post_detail.html', context)
