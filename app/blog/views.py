from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from .models import Post

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')
