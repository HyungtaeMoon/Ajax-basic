from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignupForm.as_view(), name='signup'),
    # 따로 views.py 에서 정의하지 않고 CBV 로 구현. success_url 은 profile
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('profile/', views.profile, name='profile'),
]
