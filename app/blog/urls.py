from django.urls import path

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
]
