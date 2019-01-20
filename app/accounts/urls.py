from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupForm.as_view(), name='signup'),
    # 따로 views.py 에서 정의하지 않고 CBV 로 구현. success_url 은 profile
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # LogoutView 를 사용하면 리다이렉트 되는 곳은 admin 의 logout 페이지가 사용된다
    #   templates 에서 url 다음에 ?next={{ request.path }} 와 같이 설정 필수
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
]
