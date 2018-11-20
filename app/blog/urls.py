from django.urls import path, include
from django.urls import re_path

from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.post_create, name='post_create'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('<int:post_pk>/comments/create/',
         views.comment_create, name='comment_create'),
    path('<int:post_pk>/comments/<int:pk>/edit/',
         views.comment_edit, name='comment_edit'),
    path('<int:post_pk>/comments/<int:pk>/delete/',
         views.comment_delete, name='comment_delete'),
    re_path(r'^posts\.json/$', views.post_list_json),

    re_path(r'^api/v1/', include('blog.api')),
]
