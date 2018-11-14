from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
]
