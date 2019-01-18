from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupForm.as_view(), name='signup'),
]
