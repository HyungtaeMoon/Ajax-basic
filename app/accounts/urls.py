from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupForm.as_view(), name='signup'),
    path('login/', views.LoginForm.as_view(), name='login', kwargs={'template_name': 'accounts/login.html'}),
    # LogoutView 를 사용하면 리다이렉트 되는 곳은 admin 의 logout 페이지가 사용된다
    #   templates 에서 url 다음에 ?next={{ request.path }} 와 같이 설정 필수
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
